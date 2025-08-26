import numpy as np

def euclidean_distance(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    distance = np.linalg.norm(vec1 - vec2)
    return distance

# Example usage:
v1 = [1, 2, 3]
v2 = [4, 5, 6]
print(euclidean_distance(v1, v2))  # Output: 5.196152422706632