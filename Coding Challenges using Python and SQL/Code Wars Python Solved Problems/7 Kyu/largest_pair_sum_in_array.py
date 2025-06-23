# Question: Larget pair sum in array
# Categories: 7 Kyu

def largest_pair_sum(numbers: list[int]) -> int: 
    numbers.sort()
    numbers.reverse()
    
    return numbers[0] + numbers[1]