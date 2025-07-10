# 1629A - Download More RAM

def is_still_possible_to_increase_ram(initial_ram: int, ram_cost: list[int], ram_gain: list[int]) -> bool:
    for i in range(len(ram_cost)):
        if initial_ram >= ram_cost[i]:
            return True
    
    return False

number_of_test_cases = int(input().strip())

for _ in range(number_of_test_cases):
    first_line = input().strip().split()
    n = int(first_line[0])
    k = int(first_line[1])

    a = input().strip().split()
    a = [int(num) for num in a]

    b = input().strip().split()
    b = [int(num) for num in b]

    while is_still_possible_to_increase_ram(k, a, b) is True:
        for i in range(len(a)):
            if k >= a[i]:
                k += b[i]
                a = a[:i] + a[i + 1:]
                b = b[:i] + b[i + 1:]
                break
    
    answer = k
    print(answer)