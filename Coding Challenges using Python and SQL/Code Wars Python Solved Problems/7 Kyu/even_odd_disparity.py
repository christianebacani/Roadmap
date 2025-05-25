# Question: Even odd disparity
# Categories: 7 Kyu

def solve(a: list[int | str]) -> int:
    even_numbers = []
    odd_numbers = []

    for i in range(len(a)):
        if not isinstance(a[i], int):
            continue

        if a[i] % 2 == 0:
            even_numbers.append(a[i])
        
        else:
            odd_numbers.append(a[i])
    
    return len(even_numbers) - len(odd_numbers)