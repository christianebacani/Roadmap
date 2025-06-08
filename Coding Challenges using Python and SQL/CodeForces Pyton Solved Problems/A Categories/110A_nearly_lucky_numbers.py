# 110A - Nearly Lucky Numbers

numbers = input().strip()
number_of_lucky_digits = 0

for i in range(len(numbers)):
    if numbers[i] in ['4', '7']:
        number_of_lucky_digits += 1

if number_of_lucky_digits == 4 or number_of_lucky_digits == 7:
    print('YES')

else:
    print('NO')