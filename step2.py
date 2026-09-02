import os

from dotenv import load_dotenv
# Import the Google Generative AI library so we can use its client and chat features.
from google import genai

# Create a client object that connects our Python program to the Google AI API.
# The api_key is the secret key that lets us access the Gemini service.
load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Start a chat session with the Gemini model.
# "model" tells Google which AI model to use for the conversation.
chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)

# Keep the conversation running forever until the user types exit or quit.
while True:
    # Ask the user for input and store it in the variable user_input.
    user_input = input("You: ")

    # If the user enters exit or quit (ignoring uppercase/lowercase and spaces),
    # stop the loop and end the chat session.
    if user_input.strip().lower() in ("exit", "quit"):
        break

    # Send the user's message to the AI chat and get a response.
    response = chat.send_message(user_input)

    # Extract the text content from the response object.
    reply = response.text

    # Print the AI's reply to the screen with the label "Bot:".
    print("Bot:", reply)

print("Bot: See you later!")    