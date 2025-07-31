# Question: Organise duplicate numbers in list
# Categories: 6 Kyu

def group(arr: list[int]) -> list[list[int]]:
    result = []

    for i in range(len(arr)):
        if arr.count(arr[i]) > 1:
            subarray = [arr[i]]

            elements = arr[:i] + arr[i + 1:]

            for j in range(len(elements)):
                if elements[j] == arr[i]:
                    subarray.append(elements[j]) 
            
            if subarray not in result:
                result.append(subarray)

        else:
            result.append([arr[i]])

    return result