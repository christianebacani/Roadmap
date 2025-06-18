# Question: Distance from the average
# Categories: 7 Kyu

def distances_from_average(test_list: list[int]) -> list[int]:
    average = sum(test_list) / len(test_list)
    result = []

    for i in range(len(test_list)):
        result.append(round(average - test_list[i], 2))
    return result