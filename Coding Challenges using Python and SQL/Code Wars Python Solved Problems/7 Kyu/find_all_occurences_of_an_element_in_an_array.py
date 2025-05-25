# Question: Find all occurences of an element in an array
# Categories: 7 Kyu

def find_all(array: list[int], n: int) -> list[int]:
    result = []

    for i in range(len(array)):
        if array[i] == n:
            result.append(i)
    
    return result