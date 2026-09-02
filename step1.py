import os

from dotenv import load_dotenv
# Import the Google Generative AI library so this script can use the GenAI client features.
from google import genai

# Create a GenAI client object and connect it to Google using the provided API key.
load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Start a new chat session with the Gemini 3.5 Flash Lite model.
chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)

# Send the message to the model and store the reply in the response variable.
response = chat.send_message(
    "Explain what an AI agent is in one sentence with 12 words only."
)

# Print the generated text from the AI response to the console.
print(response.text)