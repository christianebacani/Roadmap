# Queston: Geometric Progression Sequence
# Categories: 7 Kyu

def geometric_sequence_elements(first_term: int, common_ratio: int, number_of_terms: int) -> str:
    sequence = [str(first_term)]
    i = 1

    while i < number_of_terms:
        sequence.append(str(int(sequence[-1]) * common_ratio))
        i += 1
    
    return ', '.join(sequence)