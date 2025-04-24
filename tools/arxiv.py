import os
from langchain_community.utilities.arxiv import ArxivAPIWrapper
from langchain_core.tools import Tool


# --- Tool Setup ---
arxiv_api = ArxivAPIWrapper(
    top_k_results=3,
    ARXIV_MAX_QUERY_LENGTH=300,
    load_max_docs=3,
    load_all_available_meta=False,
    doc_content_chars_max=50000
)

def arxiv_search(query: str) -> str:
    return arxiv_api.run(query)

arxiv = Tool(
    name="Arxiv Search",
    func=arxiv_search,
    description="Search academic papers from Arxiv"
)
