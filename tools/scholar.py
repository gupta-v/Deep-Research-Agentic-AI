import os
from dotenv import load_dotenv
from langchain_community.tools.google_scholar import GoogleScholarQueryRun
from langchain_community.utilities.google_scholar import GoogleScholarAPIWrapper
from langchain_core.tools import Tool

load_dotenv()


# --- Tool Setup ---
scholar_api = GoogleScholarQueryRun(
    api_wrapper=GoogleScholarAPIWrapper(top_k_results=3)
)

def scholar_search(query: str) -> str:
    return scholar_api.run(query)

scholar = Tool(
    name="Google Scholar Search",
    func= scholar_search,
    description="Search academic papers from Google Scholar"
)