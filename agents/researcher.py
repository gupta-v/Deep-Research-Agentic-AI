import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_groq import ChatGroq

from tools.wikipedia import wikipedia
from tools.scholar import scholar
from tools.arxiv import arxiv
from tools.tavily import tavily

load_dotenv()

llm = ChatGroq(model="meta-llama/llama-4-maverick-17b-128e-instruct", temperature=0.2)

tools = [wikipedia, arxiv, scholar, tavily]

research_agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

