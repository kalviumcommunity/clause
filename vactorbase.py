import numpy as np
import faiss

# Example: Create some sentence embeddings (vectors)
embeddings = np.array([
    [0.1, 0.2, 0.3],
    [0.2, 0.1, 0.4],
    [0.9, 0.8, 0.7]
], dtype='float32')

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)  # L2 (Euclidean) distance
index.add(embeddings)  # Add vectors to the database

# Query: Find the nearest vector to a new embedding
query_vector = np.array([[0.15, 0.18, 0.33]], dtype='float32')
k = 2  # Top 2 nearest neighbors
distances, indices = index.search(query_vector, k)

print("Nearest indices:", indices)
print("Distances:", distances)