# Question: Pairs of integers from 0 to n
# Categories: 7 Kyu

def generate_pairs(n: int) -> list[list[int]]:
    result = []

    for i in range(n + 1):
        for j in range(n + 1):
            pair = [i, j]
            pair.sort()

            if pair not in result:
                result.append(pair)

    result.sort()
    return result