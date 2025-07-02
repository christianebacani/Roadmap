# 1473A - Replacing Elements

t = int(input().strip())

for _ in range(t):
    first_line = input().strip().split()
    n = int(first_line[0])
    d = int(first_line[1])
    
    a = input().strip().split()
    a = [int(num) for num in a]

    for i in range(len(a)):
        if a[i] <= d:
            continue

        elements = sorted(a[:i] + a[i + 1:])
        new_element = elements[0] + elements[1]

        if new_element <= d:
            a[i] = new_element
    
    possible_to_make_elements_less_than_or_equal_to_d = True

    for i in range(len(a)):
        if a[i] > d:
            possible_to_make_elements_less_than_or_equal_to_d = False
            break
    
    if possible_to_make_elements_less_than_or_equal_to_d:
        print('YES')
    
    else:
        print('NO')