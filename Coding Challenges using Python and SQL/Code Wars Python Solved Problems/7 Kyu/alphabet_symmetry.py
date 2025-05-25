# Question: Alphabet symmetry
# Categories: 7 Kyu

def solve(strings : list[str]) -> list[int]:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    result = []

    for i in range(len(strings)):
        strings[i] = strings[i].lower()
        count = 0

        for j in range(len(strings[i])):
            if (alphabets.index(strings[i][j]) + 1) == (j + 1):
                count += 1

        result.append(count)

    return result