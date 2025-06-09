import asyncio
from tools.weather_api import get_weather
from agent import weather_agent, agent_team
from autogen_agentchat.ui import Console  # Add this import

async def main():
    print("Weather chatbot. Type 'exit' to quit.")
    while True:
        user = input("You: ")
        if user.lower() == "exit":
            break
        stream = agent_team.run_stream(task=user)
        await Console(stream)

if __name__ == "__main__":
    asyncio.run(main())
