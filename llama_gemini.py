import asyncio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.google_genai import GoogleGenAI


# Define a simple calculator tool
def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a * b


# Create an agent workflow with our calculator tool
agent = FunctionAgent(
    tools=[multiply],
    llm = GoogleGenAI(
    model="models/gemini-1.5-flash", api_key= "API_KEY"
    # api_key="some key",  # uses GOOGLE_API_KEY env var by default
),
    system_prompt="You are a helpful assistant that can multiply two numbers.",
)


async def main():
    # Run the agent
    
    response = await agent.run("What is 1234 * 4567?")
    print(str(response))


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())
