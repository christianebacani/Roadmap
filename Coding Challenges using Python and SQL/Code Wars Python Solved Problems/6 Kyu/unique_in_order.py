# Question: Unique in Order
# Categories: 6 Kyu

def unique_in_order(sequence: list[str, int]) -> list[str, int]:
    answer = []

    for i in range(len(sequence)):
        if answer == []:
            answer.append(sequence[i])
            continue

        if answer[-1] != sequence[i]:
            answer.append(sequence[i])
    
    return answer