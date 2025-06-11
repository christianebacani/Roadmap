# 25A - IQ test

n = input()
numbers = input().strip().split()

numbers = [int(num) for num in numbers]
even_numbers, odd_numbers = [], []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])
    
    else:
        odd_numbers.append(numbers[i])

if len(even_numbers) < len(odd_numbers):
    print(numbers.index(even_numbers[0]) + 1)

else:
    print(numbers.index(odd_numbers[0]) + 1)