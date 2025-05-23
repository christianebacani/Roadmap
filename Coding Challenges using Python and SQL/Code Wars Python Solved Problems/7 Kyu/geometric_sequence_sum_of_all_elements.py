# Question: Geometric sequence - sum of all elements
# Categories: 7 Kyu

def geometric_sequence_sum(first_term: int, common_ratio: int, number_of_terms: int) -> int:
    sequence = [first_term]
    i = 1

    while i < number_of_terms:
        sequence.append(sequence[-1] * common_ratio)
        i += 1
    
    return sum(sequence)