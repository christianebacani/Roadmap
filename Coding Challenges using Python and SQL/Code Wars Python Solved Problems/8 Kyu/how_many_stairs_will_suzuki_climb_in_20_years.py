# Question: How many stairs will Suzuki climb in 20 years?
# Categories: 8 Kyu

def stairs_in_20(stairs: list[list[int]]) -> int:
    total = 0

    for i in range(len(stairs)):
        total += sum(stairs[i])

    answer = total * 20
    return answer