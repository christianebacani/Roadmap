# Question: Find the motif in DNA sequence
# Categories: 7 Kyu

def motif_locator(sequence: str, motif: str) -> list[int]:
    result = []

    for i in range(1, len(sequence) + 1):
        for j in range(len(sequence)):
            subsequence = sequence[j : j + i]

            if len(subsequence) != i:
                continue

            if subsequence == motif:
                result.append(j + 1)
    
    return result