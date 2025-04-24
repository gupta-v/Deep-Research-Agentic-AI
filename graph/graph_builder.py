from langgraph.graph import StateGraph, END
from state.context import AgentState
from .nodes import researcher_node, drafter_node, enhancer_node

def build_graph():
    builder = StateGraph(AgentState)

    # Define nodes
    builder.add_node("researcher", researcher_node)
    builder.add_node("drafter", drafter_node)
    builder.add_node("enhancer", enhancer_node)

    # Set entry point directly to first node
    builder.set_entry_point("researcher")

    builder.add_edge("researcher", "drafter")

    def needs_followup(state: AgentState):
        return "researcher" if state["followup_needed"] else "enhancer"

    builder.add_conditional_edges("drafter", needs_followup)
    builder.add_edge("enhancer", END)

    return builder.compile()
