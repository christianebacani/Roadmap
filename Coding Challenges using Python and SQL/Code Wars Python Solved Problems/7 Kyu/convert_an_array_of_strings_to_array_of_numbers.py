# Question: Convert an array of strings to array of numbers
# Categories: 7 Kyu

def to_float_array(arr: list[str]) -> list[int | float]: 
    result = []

    for i in range(len(arr)):
        if '.' in arr[i]:
            result.append(float(arr[i]))
        
        else:
            result.append(int(arr[i]))
    
    return result