import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.ChatCompletion.create(
#   model="gpt-4",
#   messages=[{"role": "user", "content": "Hello, AI Dungeon Master!"}]
# )

# print(response.choices[0].message.content)

print(openai.api_key)