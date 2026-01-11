from typing import TypedDict, Optional, List

class AgentState(TypedDict):
    intent: Optional[str]
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]
    messages: List[str]
