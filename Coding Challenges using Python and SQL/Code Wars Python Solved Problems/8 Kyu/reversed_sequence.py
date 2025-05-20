# Question: Reversed sequence
# Categories: 8 Kyu

def reverse_seq(number: int) -> list[int]:
    result = [i for i in range(number, 0, -1)]

    return result