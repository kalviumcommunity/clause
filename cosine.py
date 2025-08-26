import numpy as np

def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    similarity = dot_product / (norm1 * norm2)
    return similarity

# Example usage:
v1 = [1, 2, 3]
v2 = [4, 5, 6]
print(cosine_similarity(v1, v2))  # Output: 0.9746318461970762