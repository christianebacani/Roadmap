# Question: Arithmetic List!
# Categories: 7 Kyu

def seqlist(first: int, c: int, l: int) -> list[int]:
    result = [first]
    i = 1

    while i < l:
        result.append(result[-1] + c)
        i += 1

    return result