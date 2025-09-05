# Question: Flatten
# Categories: 7 Kyu

def flatten(lst: list[str | int | bool | list]) -> list[str | int | bool | list]:
    result = []

    for i in range(len(lst)):
        if not isinstance(lst[i], list):
            result.append(lst[i])
            continue

        for j in range(len(lst[i])):
            result.append(lst[i][j])
    
    return result