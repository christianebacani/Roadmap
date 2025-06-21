# 1729A - Two Elevators

t = int(input().strip())

for _ in range(t):
    test_input = input().strip().split()
    a = int(test_input[0])
    b = int(test_input[1])
    c = int(test_input[2])

    number_of_seconds_the_elev_a_comes = abs(a - 1)
    number_of_seconds_the_elev_b_comes = abs(b - c) + abs(c - 1)

    if number_of_seconds_the_elev_a_comes < number_of_seconds_the_elev_b_comes:
        print(1)
    
    elif number_of_seconds_the_elev_b_comes < number_of_seconds_the_elev_a_comes:
        print(2)
    
    else:
        print(3)