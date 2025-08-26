# ...existing code...
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
API_VERSION = os.getenv("GEMINI_API_VERSION", "v1beta")

def oneshot_prompt(example_input, example_output, user_input):
    # Construct the one-shot prompt
    prompt = (
        f"Example:\nUser: {example_input}\nAI: {example_output}\n"
        f"Now answer this:\nUser: {user_input}\nAI:"
    )
    return prompt

def get_gemini_response(prompt):
    url = f"https://generativelanguage.googleapis.com/{API_VERSION}/models/{MODEL}:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.ok:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "Error: " + response.text

if __name__ == "__main__":
    # Example for one-shot prompting
    example_input = "What is the capital of France?"
    example_output = "The capital of France is Paris."
    print("Genius Chatbot (One-shot Prompting)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        prompt = oneshot_prompt(example_input, example_output, user_input)
        response = get_gemini_response(prompt)
        print("Genius:", response)
# ...existing code...