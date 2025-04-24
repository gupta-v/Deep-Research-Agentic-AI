from langchain_groq import ChatGroq
from agents.researcher import research_agent

llm = ChatGroq(model="deepseek-r1-distill-llama-70b", temperature=0.4)

def draft_answer_with_feedback(context: str, original_query: str, max_rounds: int = 2) -> str:
    current_context = context
    history = []

    for round in range(max_rounds):
        prompt = f"""
You are an assistant drafting an answer based on this research context:

{current_context}

If you feel the information is sufficient, write the draft.
If not, return a single clarifying question to ask the researcher in this format:

[NEED_MORE_INFO] What would you like to know?
        """.strip()

        result = llm.invoke([
            ("system", "You are an academic assistant."),
            ("human", prompt)
        ])

        content = result.content.strip()
        history.append(content)

        if content.startswith("[NEED_MORE_INFO]"):
            follow_up = content[len("[NEED_MORE_INFO]"):].strip()
            new_info = research_agent.run(f"{original_query}. Clarify this: {follow_up}")
            current_context += f"\n\nAdditional Info:\n{new_info}"
        else:
            return content

    return history[-1]  # Return last attempt even if info felt insufficient
