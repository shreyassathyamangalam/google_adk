import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import uuid
from question_answering_agent.agent import question_answering_agent

load_dotenv()

async def main():
    # Create session service
    session_service_stateful = InMemorySessionService()

    initial_state = {
        "user_name": "Shreyas",
        "user_preferences": """
            I like to ride Motorcycles and read books.
            My favourite food is Mexican.
            My favourite TV show was Band of Brothers
        """,
    }

    APP_NAME = "Shreyas Bot"
    USER_ID = "shreyas_sathyamangalam"
    SESSION_ID = str(uuid.uuid4())

    # ✅ MUST AWAIT — this was the main bug
    await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state,
    )

    print("Created New Session:")
    print(f"\tSession ID: {SESSION_ID}")

    runner = Runner(
        agent=question_answering_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful
    )

    new_message = types.Content(
        role="user", parts=[types.Part(text="What is Shreyas's favourite food?")]
    )

    # Runner.run() is synchronous, but internally triggers async threads
    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Final Response: {event.content.parts[0].text}")

    print("=== Session Event Exploration ===")

    # ❗ MUST ALSO AWAIT THIS
    session = await session_service_stateful.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    print("Stored session state:", session.state)

# Run async main
asyncio.run(main())
