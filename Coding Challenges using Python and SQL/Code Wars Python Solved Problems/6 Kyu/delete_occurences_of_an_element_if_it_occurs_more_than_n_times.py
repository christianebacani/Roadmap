# Question: Delete occurences of an element if it occurs more than n times
# Categories: 6 Kyu

def delete_nth(arr: list[int], maximum_occurence: int) -> list[int]:
    answer = []

    for i in range(len(arr)):
        if answer == []:
            answer.append(arr[i])
            continue

        if (answer + [arr[i]]).count(arr[i]) <= maximum_occurence:
            answer.append(arr[i])
    
    return answer