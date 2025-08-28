# ...existing code...
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Tell me a fun fact."
output = generator(prompt, max_length=50, top_p=0.9)  # top_p set to 0.9

print(output[0]['generated_text'])
# ...existing code...