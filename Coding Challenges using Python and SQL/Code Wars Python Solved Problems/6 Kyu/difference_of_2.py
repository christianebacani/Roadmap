# Question: Difference of 2
# Categories: 6 Kyu

def twos_difference(lst: list[int]) -> list[tuple[int]]: 
    result = []

    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue

            if abs(lst[i] - lst[j]) != 2:
                continue

            if tuple(sorted([lst[i], lst[j]])) not in result:
                result.append(tuple(sorted([lst[i], lst[j]])))

    return sorted(result)