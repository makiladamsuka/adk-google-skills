import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

from agent import root_agent


async def main() -> None:
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="app",
        user_id="user1",
    )

    runner = Runner(
        agent=root_agent,
        app_name="app",
        session_service=session_service,
    )
    message = Content(
        role="user",
        parts=[Part(text="My name is Alex")],
    )

    async for event in runner.run_async(
        user_id="user1",
        session_id=session.id,
        new_message=message,
    ):
        if event.is_final_response() and event.content:
            print(event.content.parts[0].text)

    print("Session state:", session.state)
    print("Name:", session.state.get("user_name", "Guest"))
    print("Count:", session.state.get("count", 0))


if __name__ == "__main__":
    asyncio.run(main())