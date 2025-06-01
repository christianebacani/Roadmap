# Question: Numbers Which Sum of Powers of Its Digits Is The Same Number
# Categories: 7 Kyu

def eq_sum_powdig(upper_bound: int, exponent: int) -> list[int]:
    result = []

    for i in range(2, upper_bound + 1):
        number = i
        number_string = str(number)
        total = 0

        for j in range(len(number_string)):
            total += (int(number_string[j]) ** exponent)
        
        if total == number:
            result.append(number)
    
    return result