# Question: Count number of zeroes from 1 to N
# Categories: 7 Kyu

def count_zeros(number: int) -> int:
    count = 0

    for i in range(1, number + 1):
        count += str(i).count('0')
    
    return count