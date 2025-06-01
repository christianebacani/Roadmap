# Question: Summing a number's digits
# Categories: 7 Kyu

def sum_digits(number: int) -> int:
    number = list(str(number))
    sum_of_its_digits = 0

    for i in range(len(number)):
        try:
            sum_of_its_digits += abs(int(number[i]))

        except ValueError:
            continue

    return sum_of_its_digits