import logging

from agents.researcher import research_agent
from agents.drafter import draft_answer_with_feedback
from agents.enhancer import enhance_draft

logger = logging.getLogger(__name__)

def safe_add_message(state, role: str, content: str):
    if "messages" not in state:
        state["messages"] = []
    state["messages"].append({"role": role, "content": content})
    return state


def researcher_node(state):
    logger.info("🧠 Researcher called with query: %s", state["query"])

    query = state.get("followup_query") or state["query"]
    state = safe_add_message(state, "user", query)

    result = research_agent.invoke(query)
    state["research_context"].append(result)

    logger.debug("📚 Researcher result: %s", str(result)[:300])  # Truncate for readability
    state = safe_add_message(state, "assistant", f"[Researcher]:\n{result}")

    state["followup_needed"] = False
    state["followup_query"] = None
    return state


def drafter_node(state):
    logger.info("✍️ Drafter analyzing context...")

    full_context = "\n\n".join([str(entry) for entry in state["research_context"]])

    result = draft_answer_with_feedback(full_context, state["query"])

    state = safe_add_message(state, "system", "Drafter reviewing context...")

    if result.startswith("[NEED_MORE_INFO]"):
        followup = result.replace("[NEED_MORE_INFO]", "").strip()
        logger.warning("🔁 Drafter requested more info: %s", followup)

        state["followup_needed"] = True
        state["followup_query"] = followup
        state = safe_add_message(state, "assistant", f"[Drafter] Needs more info: {followup}")
    else:
        logger.info("📝 Draft generated successfully.")
        state["draft"] = result
        state["followup_needed"] = False
        state["followup_query"] = None

        state = safe_add_message(state, "assistant", f"[Drafted Answer]:\n{result}")

    return state


def enhancer_node(state):
    logger.info("🧼 Enhancer polishing the draft...")

    draft = state["draft"]
    full_context = "\n\n".join([str(entry) for entry in state["research_context"]])
    result = enhance_draft(draft, full_context)

    logger.info("✅ Enhanced answer finalized.")
    state["enhanced"] = result

    state = safe_add_message(state, "system", "Enhancer refining the draft...")
    state = safe_add_message(state, "assistant", f"[Enhanced Answer]:\n{result}")

    return state
