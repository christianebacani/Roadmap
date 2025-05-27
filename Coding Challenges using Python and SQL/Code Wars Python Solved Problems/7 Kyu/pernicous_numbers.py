# Question: Pernicious Numbers
# Categories: 7 Kyu
import math

def pernicious(n: int) -> list[int] | str:
    pernicious_numbers = []

    for i in range(2, math.floor(n) + 1):
        bit_count = bin(i)[2:].count('1')
        prime = True

        if bit_count == 1:
            continue

        for j in range(2, bit_count):
            if bit_count % j == 0:
                prime = False
                break
        
        if prime:
            pernicious_numbers.append(i)
    
    if pernicious_numbers == []:
        return 'No pernicious numbers'
    
    return pernicious_numbers