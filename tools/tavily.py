import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_core.tools import Tool

load_dotenv()

# --- Tool Setup ---
tavily_api = TavilySearch(max_results=2,
                      topic="general",
                      include_answer=True,
                      include_raw_content=True, )


def tavily_search(query: str) -> str:
    return tavily_api.invoke(query)

tavily = Tool(
    name="Tavily Search",
    func= tavily_search,
    description="Search academic papers from Arxiv"
)