# Question: Find the Parity Outlier
# Categories: 6 Kyu

def find_outlier(integers: list[int]) -> int:
    odd_numbers = []
    even_numbers = []

    for i in range(len(integers)):
        if integers[i] % 2 != 0:
            odd_numbers.append(integers[i])
        
        else:
            even_numbers.append(integers[i])
    
    if len(odd_numbers) > len(even_numbers):
        return even_numbers[0]
    
    else:
        return odd_numbers[0]