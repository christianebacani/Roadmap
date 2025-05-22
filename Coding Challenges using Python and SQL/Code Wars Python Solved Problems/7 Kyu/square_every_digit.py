# Question: Square Every Digit
# Categories: 7 Kyu

def square_digits(numbers: int) -> int:
    numbers = str(numbers)
    squares = []

    for i in range(len(numbers)):
        squares.append(str(int(numbers[i]) ** 2))
    
    return int(''.join(squares))