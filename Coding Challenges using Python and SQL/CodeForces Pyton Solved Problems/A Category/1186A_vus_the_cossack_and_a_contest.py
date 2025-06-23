# 1186A - Vus the Cossack and a Contest

test_input = input().strip().split()
number_of_participants = int(test_input[0])
number_of_pens = int(test_input[1])
number_of_notebooks = int(test_input[2])

while number_of_pens > 0 and number_of_notebooks > 0:
    if number_of_participants == 0:
        break

    number_of_participants -= 1
    number_of_pens -= 1
    number_of_notebooks -= 1

if number_of_participants == 0:
    print('YES')

else:
    print('NO')