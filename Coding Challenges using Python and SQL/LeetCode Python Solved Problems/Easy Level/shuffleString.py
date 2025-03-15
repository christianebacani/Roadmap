# 1528.) Shuffle String
# Categories: Array, String

def restoreString(s: str, indices: list[int]) -> str:
    indices_with_char = {}

    for i in range(len(indices)):
        for j in range(len(s)):
            if i == j:
                indices_with_char[indices[i]] = s[j]

    result = ''

    for i in range(len(s)):
        result += indices_with_char[i]

    return result

