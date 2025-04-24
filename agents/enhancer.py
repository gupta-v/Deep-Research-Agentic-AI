import os
import sys
from langchain_groq import ChatGroq
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

load_dotenv()


llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

def enhance_draft(draft: str, context: str) -> str:
    prompt = f"""You're a scientific editor. Refine the draft below for clarity, structure, and factual tone. Use the provided research context to validate accuracy.

Research Context:
{context}

Draft to Improve:
{draft}

Improved Answer:"""

    result = llm.invoke([
        ("system", "You are a detail-oriented scientific editor."),
        ("human", prompt)
    ])
    return result.content


if __name__ == "__main__":
    from drafter import draft_answer
    raw_draft = draft_answer("Example context from research agent.")
    final = enhance_draft(raw_draft)
    print("Enhanced Answer:\n", final)
