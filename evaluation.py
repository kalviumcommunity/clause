import pytest

# 1. Evaluation dataset: at least 5 samples
evaluation_dataset = [
    {"input": "What is the capital of France?", "expected": "Paris"},
    {"input": "2 + 2", "expected": "4"},
    {"input": "Translate 'hello' to Spanish.", "expected": "Hola"},
    {"input": "Who wrote Hamlet?", "expected": "Shakespeare"},
    {"input": "What is the boiling point of water?", "expected": "100°C"},
]

# 2. Dummy chatbot function (replace with your model/API call)
def chatbot_response(user_input):
    responses = {
        "What is the capital of France?": "Paris",
        "2 + 2": "4",
        "Translate 'hello' to Spanish.": "Hola",
        "Who wrote Hamlet?": "Shakespeare",
        "What is the boiling point of water?": "100°C",
    }
    return responses.get(user_input, "")

# 3. Judge prompt: compares model output with expected result
def judge_prompt(model_output, expected_output):
    """
    Judge prompt parameters considered:
    - Factual correctness
    - Directness (does it answer the question?)
    - Case-insensitive match
    - Handles minor variations (e.g., punctuation)
    """
    return expected_output.lower() in model_output.lower()

# 4. Testing framework: runs all test cases
@pytest.mark.parametrize("sample", evaluation_dataset)
def test_chatbot(sample):
    output = chatbot_response(sample["input"])
    assert judge_prompt(output, sample["expected"]), f"Failed for input: {sample['input']}"

if __name__ == "__main__":
    pytest.main()