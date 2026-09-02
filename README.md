# 🤖 Mini ChatGPT — Gemini AI Coding Agent

> A terminal-based AI coding agent built with Python and Google's Gemini API that can reason about tasks, use tools, interact with files, write code, and execute shell commands with user approval.

---

## 🚀 What is this project?

This project started as a simple experiment to understand how an LLM works through an API.

Step by step, it evolved from:

```text
Simple API Call
      ↓
Conversational Chatbot
      ↓
Conversation Memory
      ↓
Function Calling
      ↓
Tool Execution
      ↓
AI Coding Agent 🤖
```

The final result is a **terminal-based AI agent** that can interact with the user's local environment using Python tools.

Unlike a normal chatbot that only generates text, this agent can decide when it needs to perform an action and request the appropriate tool.

---

# ✨ Features

The AI Coding Agent can:

- 📂 List files and directories
- 📖 Read the contents of files
- ✍️ Create and write files
- 💻 Run shell commands
- 🧠 Decide which tool is required for a task
- 🔄 Continue working until the task is completed
- 💬 Maintain conversation history during the session
- 🛡️ Ask for user confirmation before executing shell commands

---

# 🧠 How Does the AI Agent Work?

The agent follows a tool-calling loop.

```text
                    USER REQUEST
                         │
                         ▼
                  🤖 GEMINI MODEL
                         │
                         ▼
              Does the task require a tool?
                   │              │
                 NO               YES
                   │              │
                   ▼              ▼
              Final Answer    Select Tool
                                   │
                                   ▼
                           Python Executes Tool
                                   │
                                   ▼
                            Tool Result
                                   │
                                   ▼
                          Send Result to Gemini
                                   │
                                   ▼
                        Continue Working?
                           │        │
                          YES       NO
                           │        │
                           ▼        ▼
                      Use Tool   Final Answer
                        Again
```

This is the core idea behind an **AI agent**:

> The LLM does not directly execute Python code. It decides which action should be taken. Python executes that action and returns the result to the LLM.

---

# 🛠️ Available Tools

The agent currently has four tools.

---

## 📂 `list_files()`

Lists files and directories at a specified location.

Example request:

```text
Show me the files in this project.
```

The model may request:

```python
list_files(path=".")
```

---

## 📖 `read_file()`

Reads the contents of a file.

Example request:

```text
Read my notes.txt file and summarize it.
```

The agent may request:

```python
read_file(path="notes.txt")
```

---

## ✍️ `write_file()`

Creates or writes content to a file.

Example request:

```text
Create a Python file that prints Hello World.
```

The model may request:

```python
write_file(
    path="hello.py",
    content="print('Hello World')"
)
```

---

## 💻 `run_command()`

Runs shell commands.

For safety, the agent asks for confirmation before executing a command.

Example:

```text
Run 'python hello.py'? [y/N]
```

The command will only run if the user approves it.

---

# 🧩 Project Structure

```text
Mini-ChatGPT/
│
├── .env
├── .env.example
├── .gitignore
│
├── agent.py
│
├── step1.py
├── step2.py
├── step3.py
│
├── notes.txt
│
├── requirements.txt
├── pyproject.toml
├── uv.lock
│
├── README.md
│
├── src/
│   └── mini_chatgpt/
│       └── __init__.py
│
└── snake-game/
    ├── README.md
    ├── constants.py
    ├── game_logic.py
    ├── renderer.py
    ├── requirements.txt
    └── snake.py
```

---

# 📚 Development Journey

This repository also contains the different stages used to understand how the final AI agent works.

---

## Step 1 — Connecting Python with Gemini

The first step was simply connecting Python with the Gemini API.

```text
Python Program
       │
       ▼
Gemini API
       │
       ▼
   AI Response
```

The goal was to understand:

- How to create a Gemini client
- How to authenticate using an API key
- How to send prompts
- How to receive responses

---

## Step 2 — Building a Conversational Chatbot

The next step was building a chatbot capable of maintaining a conversation.

```text
User Message
      │
      ▼
Conversation History
      │
      ▼
 Gemini Model
      │
      ▼
AI Response
      │
      ▼
Add Response to History
```

This demonstrated an important concept:

> Language models need conversation context to understand previous messages.

---

## Step 3 — Understanding Function Calling

The next step introduced **tools and function calling**.

The model was given information about a Python function:

```text
User asks a question
        │
        ▼
Gemini analyzes the request
        │
        ▼
Does it need a tool?
        │
        ▼
Gemini requests a function call
        │
        ▼
Python executes the function
        │
        ▼
Result returned to Gemini
        │
        ▼
Gemini generates the final answer
```

This was the transition from a simple chatbot to an **AI agent architecture**.

---

# 🤖 Final Project — AI Coding Agent

The final agent combines everything learned in the previous steps.

The agent can:

```text
UNDERSTAND
    ↓
REASON
    ↓
CHOOSE A TOOL
    ↓
EXECUTE ACTION
    ↓
OBSERVE RESULT
    ↓
CONTINUE OR RESPOND
```

The core agent loop works like this:

```text
while task is not complete:

    Send conversation to Gemini

    if Gemini requests a tool:
        Execute the tool
        Send the result back to Gemini

    else:
        Return the final response
        Stop
```

---

# 🎮 Example: Building a Snake Game

The AI agent was tested by asking it to help create a Snake Game project.

The agent used multiple tools to work on the project.

Example workflow:

```text
USER:
Create a Snake Game project.
        │
        ▼
GEMINI:
Analyzes the task
        │
        ▼
write_file()
        │
        ▼
Creates Python source files
        │
        ▼
run_command()
        │
        ▼
Installs dependencies
        │
        ▼
read_file()
        │
        ▼
Reads existing code
        │
        ▼
write_file()
        │
        ▼
Updates / refactors code
        │
        ▼
run_command()
        │
        ▼
Verifies the program
```

The Snake Game project was also refactored into multiple files to separate responsibilities.

```text
constants.py
      ↓
Game settings and constants

game_logic.py
      ↓
Snake movement and game logic

renderer.py
      ↓
Drawing and graphics

snake.py
      ↓
Main game loop
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

Move into the project:

```bash
cd Mini-ChatGPT
```

---

## Option 1 — Using UV

This project uses `uv` for dependency management.

Install dependencies:

```bash
uv sync
```

---

## Option 2 — Using pip

Install dependencies manually:

```bash
pip install -r requirements.txt
```

---

# 🔑 Gemini API Setup

The project requires a Gemini API key.

## Step 1

Create a `.env` file in the root directory.

```text
Mini-ChatGPT/
│
├── .env
├── agent.py
└── ...
```

---

## Step 2

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Step 3

The application loads the key using environment variables.

```python
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
```

---

# 🔒 Security

The `.env` file contains sensitive information and should never be uploaded to GitHub.

The project uses `.gitignore` to prevent this.

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

A safe template is included:

```text
.env.example
```

Example:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Never commit your actual API key.

---

# ▶️ Running the Agent

After setting up your API key, run:

```bash
python agent.py
```

If you are using `uv`:

```bash
uv run agent.py
```

You should see:

```text
You:
```

Now give the agent a task.

Example:

```text
You: Show me all files in the current directory.
```

Or:

```text
You: Read notes.txt and summarize it.
```

Or:

```text
You: Create a Python file that prints Hello World.
```

---

# 💬 Example Interaction

```text
You: Read notes.txt and summarize it.
```

The agent may decide:

```text
tool: read_file({'path': 'notes.txt'})
```

Python executes the tool.

The result is sent back to Gemini.

Then Gemini responds:

```text
Bot: The file explains the basic concepts of AI agents and tool usage.
```

---

# 🛡️ Safety Mechanism

Running shell commands can potentially modify the user's system.

Therefore, the agent asks for permission before executing a command.

Example:

```text
tool: run_command({'command': 'python app.py'})

Run 'python app.py'? [y/N]
```

The user controls whether the command is executed.

```text
y → Execute command

N → Reject command
```

---

# 🧰 Technologies Used

- 🐍 Python
- 🤖 Google Gemini API
- 🧠 Gemini Function Calling
- 🔧 Python Tools
- 🌱 Environment Variables
- 📦 UV
- 💻 Subprocess
- 📁 File System Operations

---

# 🎯 What I Learned

Through this project, I learned:

- How to work with an LLM API
- How to create conversational applications
- How conversation history works
- How LLMs use context
- How function calling works
- How AI agents interact with tools
- How to manually implement an agent loop
- How to execute Python functions requested by an LLM
- How to return tool results back to the model
- How to protect API keys using `.env`
- How to prevent secrets from being uploaded to GitHub

---

# 🔮 Future Improvements

Possible improvements include:

- [ ] Add more tools
- [ ] Add file deletion capabilities with safety checks
- [ ] Add code execution in a sandbox
- [ ] Improve command security
- [ ] Add streaming responses
- [ ] Add persistent conversation memory
- [ ] Add a web interface
- [ ] Support multiple LLM providers
- [ ] Add automated testing
- [ ] Improve error handling
- [ ] Add a tool permission system
- [ ] Add project-level context awareness

---

# 🧠 Key Concept Behind This Project

A normal chatbot mainly does this:

```text
INPUT
  ↓
LLM
  ↓
TEXT OUTPUT
```

An AI agent can do more:

```text
INPUT
  ↓
LLM
  ↓
DECISION
  ↓
TOOL
  ↓
ACTION
  ↓
OBSERVATION
  ↓
LLM
  ↓
FINAL RESPONSE
```

That loop is the main idea explored in this project.

---

# 📌 Final Takeaway

This project is not just a simple chatbot.

It is a learning project focused on understanding how an **AI Agent works internally**.

The final application combines:

```text
LLM
+
TOOLS
+
AGENT LOOP
+
MEMORY
+
ACTION
```

to create a basic terminal-based AI Coding Agent.

---

## ⭐ If you found this project interesting

Feel free to explore the different development steps:

```text
step1.py
   ↓
Basic Gemini API Connection

step2.py
   ↓
Conversational Chat

step3.py
   ↓
Function Calling

agent.py
   ↓
Final AI Coding Agent
```

---

# 👨‍💻 Author

**Mohd Sahil**

Built as a hands-on project while learning:

```text
AI Agents
LLMs
Function Calling
Python Automation
Gemini API
```

---

⭐ **If you like this project, consider giving the repository a star!**