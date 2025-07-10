# Question: Count the Digit
# Categories: 7 Kyu

def nb_dig(n: int, d: int) -> int:
    squared_digits = []

    for i in range(0, n + 1):
        squared_digits.append(i ** 2)
    
    total = 0

    for i in range(len(squared_digits)):
        total += (str(squared_digits[i]).count(str(d)))
    
    return total