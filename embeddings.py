# Install the library first:
# pip install sentence-transformers

from sentence_transformers import SentenceTransformer

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example sentences
sentences = [
    "This is an example sentence.",
    "Embeddings convert text to vectors."
]

# Generate embeddings
embeddings = model.encode(sentences)

print(embeddings)  # Each sentence is now a vector (numpy array)