# ...existing code...
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Tell me a joke."
output = generator(prompt, max_length=50, top_k=50)  # top_k set to 50

print(output[0]['generated_text'])
# ...existing code...