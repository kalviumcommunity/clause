Genius Chatbot Project
Genius is a simple Python-based chatbot that interacts with users using the Gemini API. It currently runs in the terminal and allows users to chat with an AI assistant by providing their API keys securely through environment variables.

Features
Zero-shot prompting: The chatbot responds to user input without prior examples.
Uses Google Gemini API for generating responses.
API keys and model configuration are loaded from a .env file for security.
Simple command-line interface for chatting.
How it Works
The user provides their API key and model details in a .env file.
The chatbot script loads these credentials and connects to the Gemini API.
Users can type messages and receive AI-generated responses in real time.
Getting Started
Clone this repository.
Create a .env file with your Gemini API key and (optionally) model/version.
Run python BasicUserPrompt.py to start chatting.
Example .env file
GENAI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.0-flash
GEMINI_API_VERSION=v1beta
Future Plans
Develop a full-featured web application for Genius with a modern UI.
Add support for advanced prompting techniques (few-shot, system prompts, etc.).
Enable conversation history and user authentication.
Deploy the app for public use.
This project is a starting point for building a more advanced AI assistant. Stay tuned for updates!

...