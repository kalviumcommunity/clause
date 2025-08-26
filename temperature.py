# pip install transformers

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Once upon a time,"
temperature = 0.7  # You can set this between 0.1 (less random) and 2.0 (more random)

output = generator(prompt, max_length=50, temperature=temperature)
print(output[0]['generated_text']) 