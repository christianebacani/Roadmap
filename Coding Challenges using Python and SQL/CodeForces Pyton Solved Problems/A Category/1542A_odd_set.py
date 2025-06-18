# 1542A - Odd Set

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    numbers = input().strip().split()
    numbers = [int(num) for num in numbers]

    odd_numbers, even_numbers = [], []

    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            odd_numbers.append(numbers[i])
        
        else:
            even_numbers.append(numbers[i])
    
    if len(odd_numbers) >= len(even_numbers):
        total_possible_pairs = len(odd_numbers)
    
    else:
        total_possible_pairs = len(even_numbers)
    
    pairs = []

    for i in range(total_possible_pairs):
        try:
            pairs.append([odd_numbers[i], even_numbers[i]])

        except IndexError:
            pass
    
    if len(pairs) == n:
        print('Yes')
    
    else:
        print('No')