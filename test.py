import os
import asyncio
from openai import OpenAI
from agents import Agent, Runner, trace
from dotenv import load_dotenv


# Set up
load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

# User Input
messages = [{"role": "user", "content": "Hello, DM! Where am I?"}]

# DM Setup
dm_instructions = f"""
You are a creative and immersive Dungeon Master for a fantasy tabletop RPG.
Guide the player through an adventure.
Describe the environment vividly, respond to player actions, and introduce challenges or NPCs dynamically.
The player will type their actions, and you respond with what happens next.
Consider briefly describing sounds or scents to further immerse the player.
Clarify the presence of any immediate points of interest or paths in the environment.
Optionally, hint at lingering dangers without revealing specifics to build suspense.
Introduce subtle environmental cues (e.g., tracks, markings) to entice exploration."""

agent = Agent(name="DM", instructions=dm_instructions, model="gpt-4.1-nano")

# Making function Async
async def main():
    with trace("Hello World"):
        result = await Runner.run(agent, messages)
        print(result.final_output)

# Initiate the session
if __name__ == "__main__":
    asyncio.run(main())
