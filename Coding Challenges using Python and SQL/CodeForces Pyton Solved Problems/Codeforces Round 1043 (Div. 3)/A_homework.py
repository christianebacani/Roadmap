# A - Homework

number_of_test_cases = int(input().strip())

for _ in range(number_of_test_cases):
    n = int(input().strip())
    a = input().strip()
    m = int(input().strip())
    b = input().strip()
    c = input().strip()

    for i in range(len(c)):
        if c[i] == 'V':
            a = b[0] + a
        
        else:
            a = a + b[0]
        
        b = b[1:]
    
    print(a)