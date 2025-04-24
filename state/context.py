from typing import TypedDict, Annotated, List, Optional

class AgentState(TypedDict):
    query: str
    research_context: Annotated[List[str], "Raw info gathered"]
    draft: Annotated[Optional[str], "Drafted answer"]
    enhanced: Annotated[Optional[str], "Final enhanced answer"]
    followup_needed: Annotated[bool, "True if drafter wants more info"]
    followup_query: Annotated[Optional[str], "Query to send to researcher"]
    messages: Annotated[List[dict], "Conversation history"]

