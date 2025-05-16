# Question: Sum of Digits / Digital Root
# Categories: 6 Kyu

def digital_root(n: int) -> int:
    number_string = str(n)

    while len(number_string) != 1:
        sum = 0

        for i in range(len(number_string)):
            sum += int(number_string[i])

        number_string = str(sum)
    
    return int(number_string)