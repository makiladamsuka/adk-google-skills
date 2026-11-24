from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-flash-latest',
    name='root_agent',
    description="Extracts a user's name and stores it in session state.",
    instruction="Extract the user's name. Return ONLY the name.",
    output_key='user_name',
)
