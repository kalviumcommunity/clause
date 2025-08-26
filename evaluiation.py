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

if __name__ == "__main__":
    pytest.main()