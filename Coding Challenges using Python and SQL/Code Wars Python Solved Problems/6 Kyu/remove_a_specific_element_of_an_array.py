# Question: Remove a Specific Element of an Array
# Categories: 6 Kyu

def select_subarray(arr: list[int]) -> list:
    absolute_quotients = []

    for i in range(len(arr)):
        if i == 0:
            subarray = arr[i + 1:]
        
        elif i == len(arr) - 1:
            subarray = arr[:i]
        
        else:
            subarray = arr[:i] + arr[i + 1:]
        
        sub_product = 1
        sub_sum = 0

        for j in range(len(subarray)):
            sub_product *= subarray[j]
            sub_sum += subarray[j]

        try:
            quotient = abs(sub_product / sub_sum)
            absolute_quotients.append(quotient)

        except ZeroDivisionError:
            continue

    minimum_absolute_quotients = min(absolute_quotients)
    subarrays = []

    for i in range(len(arr)):
        if i == 0:
            subarray = arr[i + 1:]
        
        elif i == len(arr) - 1:
            subarray = arr[:i]
        
        else:
            subarray = arr[:i] + arr[i + 1:]
        
        sub_product = 1
        sub_sum = 0

        for j in range(len(subarray)):
            sub_product *= subarray[j]
            sub_sum += subarray[j]
        
        try:
            quotient = abs(sub_product / sub_sum)

            if quotient == minimum_absolute_quotients:
                subarrays.append(subarray)

        except ZeroDivisionError:
            continue

    answer = []

    for i in range(len(subarrays)):
        for j in range(len(arr)):
            if arr[j] not in subarrays[i]:
                answer.append([j, arr[j]])
                break

    answer = sorted(answer)
    
    if len(answer) == 1:
        return answer[0]

    return answer