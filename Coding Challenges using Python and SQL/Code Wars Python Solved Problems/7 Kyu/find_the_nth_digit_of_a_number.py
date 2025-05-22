# Question: Find the nth Digit of a Number
# Categories: 7 Kyu

def find_digit(num: int, nth: int) -> int:
    if nth < 1:
        return -1

    num = str(num)[::-1]

    if nth > len(num):
        return 0
    
    for index, digit in enumerate(num):
        index += 1

        if index == nth:
            return int(digit)