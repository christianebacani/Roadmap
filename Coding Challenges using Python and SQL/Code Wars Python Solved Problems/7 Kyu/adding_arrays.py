# Question: Adding Arrays
# Categories: 7 Kyu

def arr_adder(arr: list[str]) -> list[str]:
    result = ''
    total_columns = len(arr[0])

    for i in range(total_columns):
        for j in range(len(arr)):
            if arr[j][i].isalpha():
                result += arr[j][i]
            
            else:
                result += ' '

        result += ' '

    return ' '.join(result.split())