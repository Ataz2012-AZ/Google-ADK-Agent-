from google.adk.tools.google_search_tool import google_search

math_agent = Agent(
    model='gemini-3.5-flash',
    name='math_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',

     tools=[
        math_agent_tool,
    ]
)
