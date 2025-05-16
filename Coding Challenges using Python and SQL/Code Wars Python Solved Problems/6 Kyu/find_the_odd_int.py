# Question: Find the odd int
# Categories: 6 Kyu

def find_it(seq: list[int]) -> int:
    for i in range(len(seq)):
        if seq.count(seq[i]) % 2 != 0:
            return seq[i]