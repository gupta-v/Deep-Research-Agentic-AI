# main.py

from graph.graph_builder import build_graph

graph = build_graph()

def initialize(query):
    return {
        "query": query,
        "research_context": [],
        "draft": None,
        "enhanced": None,
        "followup_needed": False,
        "followup_query": None,
        "messages": [],
    }

# Only run the graph if main.py is executed directly (CLI)
if __name__ == "__main__":
    query = input("Enter your research query: ")
    state = initialize(query)
    result = graph.invoke(state)

    print("\n=== FINAL ENHANCED ANSWER ===\n")
    print(result["enhanced"])
