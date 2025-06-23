# A - Race

number_of_test_cases = int(input().strip())

for _ in range(number_of_test_cases):
    test_input = input().strip().split()
    a = int(test_input[0])
    x = int(test_input[1])
    y = int(test_input[2])

    possible_starting_point = []

    for starting_point in range(min([x, y]), max([x, y]) + 1):
        if (abs(starting_point - x) < abs(a - x)) and (abs(starting_point - y) < abs(a - y)):
            possible_starting_point.append(starting_point)
    
    if possible_starting_point != []:
        print('YES')
    
    else:
        print('NO')