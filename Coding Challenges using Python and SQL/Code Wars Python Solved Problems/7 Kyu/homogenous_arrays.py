# Question: Homogenous arrays
# Categories: 7 Kyu

def filter_homogenous(arrays: list[list[str | int]]) -> list[list[str | int]]:
    result = []

    for i in range(len(arrays)):
        if arrays[i] == []:
            continue

        string_count = 0
        integer_count = 0

        for j in range(len(arrays[i])):
            if isinstance(arrays[i][j], str):
                string_count += 1
            
            else:
                integer_count += 1

        if string_count == len(arrays[i]) or integer_count == len(arrays[i]):
            result.append(arrays[i])
    
    return result