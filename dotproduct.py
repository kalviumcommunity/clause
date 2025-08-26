import numpy as np

def dot_product_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2)

# Example usage:
v1 = [1, 2, 3]
v2 = [4, 5, 6]
print(dot_product_similarity(v1, v2))  # Output: 32