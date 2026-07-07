from pydantic import BaseModel
class TicketInput(BaseModel):
    text: str
    metadata: dict = {}
class TicketOutput(BaseModel):
    category: str
    priority: str
    next_tool: str
    reasoning: str
    why: str
    trace: list
    tool_output: str