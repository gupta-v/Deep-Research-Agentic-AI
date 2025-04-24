import os
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_core.tools import Tool

# --- Tool Setup ---
wiki_api = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(doc_content_chars_max=5000, top_k_results=3)
)

def wiki_search(query: str) -> str:
    return wiki_api.run(query)

wikipedia = Tool(
    name="Wikipedia",
    func=wiki_search,
    description="Search Wikipedia articles for general knowledge"
)