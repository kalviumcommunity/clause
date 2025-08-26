import pytest

# Example evaluation dataset: list of (input, expected_output) pairs
evaluation_dataset = [
    {"input": "What is the capital of France?", "expected": "Paris"},
    {"input": "2 + 2", "expected": "4"},
    {"input": "Translate 'hello' to Spanish.", "expected": "Hola"},
]

# Dummy chatbot function for demonstration
def chatbot_response(user_input):
    # Replace with your actual model/API call
    responses = {
        "What is the capital of France?": "Paris",
        "2 + 2": "4",
        "Translate 'hello' to Spanish.": "Hola",
    }
    return responses.get(user_input, "")

@pytest.mark.parametrize("sample", evaluation_dataset)
def test_chatbot(sample):
    output = chatbot_response(sample["input"])
    assert sample["expected"].lower() in output.lower()


def structured_output_prompt(question):
    prompt = (
        f"Answer the following question and format your response as JSON:\n"
        f"Question: {question}\n"
        f"Response format:\n"
        f'{{"answer": "...", "explanation": "..."}}\n'
        f"Answer:"
    )
    return prompt

# Example usage:
question = "What is the capital of Germany?"
prompt = structured_output_prompt(question)
print(prompt)
# Send 'prompt' to your LLM API for a structured (JSON) response.

if __name__ == "__main__":
    pytest.main()