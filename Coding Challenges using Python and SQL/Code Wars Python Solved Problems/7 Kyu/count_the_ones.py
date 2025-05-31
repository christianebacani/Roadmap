# Question: Count the Ones
# Categories: 7 Kyu

def hamming_weight(number: int) -> int:
    return bin(number)[2:].count('1')