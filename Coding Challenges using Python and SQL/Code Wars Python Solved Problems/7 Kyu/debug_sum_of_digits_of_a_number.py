# Question: Debug Sum of Digits of a Number
# Categories: 7 Kyu

def get_sum_of_digits(num: int) -> int:
    sum = 0
    digits = list(str(num))
    for x in digits:
        sum += int(x)
    return sum