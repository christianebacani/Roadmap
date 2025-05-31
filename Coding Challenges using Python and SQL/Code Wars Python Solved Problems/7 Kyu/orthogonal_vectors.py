# Question: Orthogonal Vectors
# Categories: 7 Kyu

def is_orthogonal(first_vector: list[int], second_vector: list[int]) -> bool: 
    total_vectors = len(first_vector)
    dot_products = 0

    for i in range(total_vectors):
        dot_products += (first_vector[i] * second_vector[i])

    return dot_products == 0