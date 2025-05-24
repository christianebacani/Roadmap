# Question: Convert numnber to reversed array of digits
# Categories: 8 Kyu

def digitize(n: int) -> list[int]:
    numbers = str(n)[::-1]
    result = []
    
    for i in range(len(numbers)):
        result.append(int(numbers[i]))
    
    return result