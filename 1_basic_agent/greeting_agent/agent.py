from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Greeting Agent",
    instruction="""
    You are a helpful assistant that greets the user politely. 
    Ask for the user's name and greet them politely by name.
    """
)
