import os

from dotenv import load_dotenv
import json
from google import genai
from google.genai import types


load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ---------------- TOOL ----------------

def read_file(path: str):
    """Read a text file and return its content."""

    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"File {path} not found."


# ---------------- TOOL SCHEMA ----------------

read_file_declaration = types.FunctionDeclaration(
    name="read_file",
    description="Read a text file and return its content.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "Path of the file to read"
            }
        },
        "required": ["path"]
    }
)


tools = [
    types.Tool(
        function_declarations=[
            read_file_declaration
        ]
    )
]


# ---------------- CONVERSATION ----------------

contents = [
    types.Content(
        role="user",
        parts=[
            types.Part(
                text="What's inside the notes.txt? Summarize it in one line."
            )
        ]
    )
]


# ---------------- AGENT LOOP ----------------

while True:

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=contents,
        config=types.GenerateContentConfig(
            tools=tools,
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            )
        )
    )


    # Model response ko conversation history mein add karo
    contents.append(response.candidates[0].content)


    # Function calls nikalo
    function_calls = response.function_calls


    # Agar tool call nahi hai, model ka final answer aa gaya
    if not function_calls:

        print("Bot:", response.text)
        break


    # Har requested function call execute karo
    for function_call in function_calls:

        print(
            f"Model wants to run: "
            f"{function_call.name}({dict(function_call.args)})"
        )


        # Tool execute karo
        if function_call.name == "read_file":

            result = read_file(
                **dict(function_call.args)
            )


        # Tool result ko Gemini ko wapas bhejo
        contents.append(
            types.Content(
                role="user",
                parts=[
                    types.Part.from_function_response(
                        name=function_call.name,
                        response={
                            "result": result
                        }
                    )
                ]
            )
        )