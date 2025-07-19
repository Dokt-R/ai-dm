import os
from openai import OpenAI
from agents import Agent, Runner, trace
from dotenv import load_dotenv



# Set up
load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

# User Input
messages = [{"role": "user", "content": "Hello, AI Dungeon Master! Roll a d20 for me."}]

# DM Response
response = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)

answer = response.choices[0].message.content

print(answer)