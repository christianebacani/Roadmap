# Question: Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
# Categories: 6 Kyu

def sum_dig_pow(a: int, b: int) -> list[int]:
    answer = []

    for i in range(a, b + 1):
        number = i
        string_number = str(i)

        total = 0
    
        for j in range(len(string_number)):
            total += (int(string_number[j]) ** (j + 1))
        
        if number == total:
            answer.append(number)
    
    answer.sort()
    return answer