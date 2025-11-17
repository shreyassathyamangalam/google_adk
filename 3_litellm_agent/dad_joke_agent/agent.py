import os
import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


model = LiteLlm(
    model="openai/gpt-4o-mini",
    api_key = os.getenv("OPENAI_API_KEY")
)

def get_dad_joke():
    jokes=[
        "Why did the chicken cross the road? to get to the other side!",
        "What do you call a belt made of watches? A waist of time!",
        "What do you call fake spaghetti? An impasta!"
    ]
    
    return random.choice(jokes)
    

root_agent = Agent(
    name="dad_joke_agent",
    model=model,
    description="Dad Joke Agent",
    instruction="""
    You are a helpful assistant that can tell dad jokes.
    Only use the tool 'get_dad_joke' to tell jokes.
    """,
    tools=[get_dad_joke],
)
