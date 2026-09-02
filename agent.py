import os
import subprocess

from dotenv import load_dotenv
from google import genai
from google.genai import types


# ---------------- CONFIG ----------------
load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-3.5-flash-lite"


SYSTEM_PROMPT = """You are a coding agent running in the user's terminal.
You can list files, read files, write files, and run shell commands.
Use your tools to complete the user's task, then briefly summarize what you did.
The working directory is the folder the user launched you from."""


# ---------------- TOOLS ----------------

def list_files(path="."):
    entries = []

    for entry in os.scandir(path):
        entries.append(
            entry.name + ("/" if entry.is_dir() else "")
        )

    return "\n".join(sorted(entries)) or "(empty directory)"


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

    return f"Saved {path} ({len(content)} characters)"


def run_command(command):

    answer = input(
        f"Run '{command}'? [y/N] "
    )

    if answer.strip().lower() != "y":
        return "The user declined to run this command."

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        timeout=120
    )

    output = (
        result.stdout + result.stderr
    ).strip()

    return output or (
        f"(no output, exit code {result.returncode})"
    )


# ---------------- TOOL DICTIONARY ----------------

TOOLS = {
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file,
    "run_command": run_command,
}


# ---------------- GEMINI TOOL SCHEMAS ----------------

list_files_declaration = types.FunctionDeclaration(
    name="list_files",
    description="List files and directories at a path.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "Directory to list."
            }
        }
    }
)


read_file_declaration = types.FunctionDeclaration(
    name="read_file",
    description="Read the contents of a file.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "File path to read."
            }
        },
        "required": ["path"]
    }
)


write_file_declaration = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a file.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "File path to write."
            },
            "content": {
                "type": "string",
                "description": "Content to write."
            }
        },
        "required": [
            "path",
            "content"
        ]
    }
)


run_command_declaration = types.FunctionDeclaration(
    name="run_command",
    description="Run a shell command after asking the user for confirmation.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "command": {
                "type": "string",
                "description": "Shell command to run."
            }
        },
        "required": ["command"]
    }
)


GEMINI_TOOLS = [
    types.Tool(
        function_declarations=[
            list_files_declaration,
            read_file_declaration,
            write_file_declaration,
            run_command_declaration
        ]
    )
]


# ---------------- RUN TOOL ----------------

def run_tool(function_call):

    name = function_call.name

    args = dict(function_call.args)

    print(f"  tool: {name}({args})")

    try:

        if name not in TOOLS:
            return f"Error: unknown tool '{name}'"

        return str(
            TOOLS[name](**args)
        )

    except Exception as exc:

        return f"Error: {exc}"


# ---------------- AGENT LOOP ----------------

def run_agent(contents):

    while True:

        response = client.models.generate_content(

            model=MODEL,

            contents=contents,

            config=types.GenerateContentConfig(

                system_instruction=SYSTEM_PROMPT,

                tools=GEMINI_TOOLS,

                automatic_function_calling=(
                    types.AutomaticFunctionCallingConfig(
                        disable=True
                    )
                )
            )
        )

        # Get function calls requested by Gemini
        function_calls = response.function_calls

        # Add Gemini's response to conversation history
        contents.append(
            response.candidates[0].content
        )

        # No function calls means Gemini gave final answer
        if not function_calls:

            answer = response.text or ""

            print("Bot:", answer)

            return answer

        # Execute every requested function
        for function_call in function_calls:

            result = run_tool(
                function_call
            )

            # Send tool result back to Gemini
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


# ---------------- MAIN PROGRAM ----------------

def main():

    contents = []

    while True:

        user_input = input(
            "You: "
        ).strip()

        if not user_input:
            continue

        if user_input.lower() in {
            "exit",
            "quit",
            "bye"
        }:

            print(
                "Goodbye."
            )

            break

        # Add user message to history
        contents.append(

            types.Content(

                role="user",

                parts=[

                    types.Part(
                        text=user_input
                    )
                ]
            )
        )

        run_agent(contents)


# ---------------- START ----------------

if __name__ == "__main__":

    main()
