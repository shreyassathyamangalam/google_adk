from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime


LLM = "gemini-2.0-flash"

def get_current_time() -> dict:
    """function to get current time using datetime in the format YYYY-MM-DD HH:MM:SS"""
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    name="tool_agent",
    model=LLM,
    description="Tool Agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - get_current_time
    """,
    # tools=[google_search],
    tools=[get_current_time],
    # tools=[google_search, get_current_time] -> does not work
)
