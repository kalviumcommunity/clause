# Genius Chatbot Project

Genius is a Python-based AI chatbot that interacts with users via the Google Gemini API. It runs in the terminal and supports multiple prompting techniques, including zero-shot, one-shot, and multi-shot. Genius securely loads API keys and configuration from environment variables and is designed for easy extension and integration.

---

## Features

- **Zero-shot, One-shot, and Multi-shot Prompting:** Flexible prompting strategies for different use cases.
- **Google Gemini API Integration:** Uses Gemini for advanced conversational AI.
- **Secure API Key Management:** Credentials loaded from a `.env` file.
- **Command-line Interface:** Simple and interactive terminal chat.
- **Extensible Design:** Easily add new features, prompting styles, or connect to other APIs.
- **Evaluation & Testing:** Includes sample evaluation datasets and testing framework.
- **Vector Database Integration:** Supports semantic search and retrieval-augmented generation.

---

## How It Works

1. **Configuration:**  
   Add your Gemini API key and model details to a `.env` file.
2. **Prompting:**  
   Genius supports zero-shot (no examples), one-shot (single example), and multi-shot (multiple examples) prompting.
3. **Chat:**  
   Run the chatbot script, type your message, and receive AI-generated responses in real time.
4. **Evaluation:**  
   Use the included evaluation dataset and testing framework to validate chatbot responses.
5. **Vector Search:**  
   Integrate with FAISS or other vector databases for semantic search and context retrieval.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/genius-chatbot.git
cd genius-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
*Typical dependencies: `requests`, `python-dotenv`, `faiss-cpu`, `sentence-transformers`*

### 3. Create a `.env` File

```env
GENAI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.0-flash
GEMINI_API_VERSION=v1beta
```

### 4. Run the Chatbot

```bash
python BasicUserPrompt.py
```
Or try advanced prompting:
```bash
python oneshot.py
python multishot.py
```

---

## Example Usage

```
You: What is the capital of France?
Genius: The capital of France is Paris.
```

---

## Prompting Techniques

- **Zero-shot:** No examples, just the user’s question.
- **One-shot:** Includes one example Q&A before the user’s question.
- **Multi-shot:** Includes several example Q&A pairs to guide the model’s style and behavior.
- **Chain of Thought:** Prompts the model to reason step-by-step.
- **Structured Output:** Asks the model to reply in a specific format (e.g., JSON).

---

## Evaluation & Testing

- Use `evaluiation.py` to run automated tests on chatbot responses.
- Add new test cases to the evaluation dataset for continuous improvement.

---

## Vector Database Integration

- Store and search embeddings using FAISS or other vector databases.
- Enable semantic search and retrieval-augmented generation for advanced use cases.

---

## Extending Genius

- Add new prompting styles or system/user prompts using the RTFC framework.
- Integrate with other APIs or databases.
- Build a web UI or deploy as a cloud service.

---

## Future Plans

- Develop a full-featured web application with a modern UI.
- Add support for advanced prompting (few-shot, system prompts, function calling).
- Enable conversation history and user authentication.
- Deploy for public use.

---

## Contributing

Pull requests are welcome! Please submit your improvements, bug fixes, or new features.

---

## License

MIT License

---

## Contact

For questions or support, open an issue or contact [your-email@example.com](mailto:your-email@example.com).
