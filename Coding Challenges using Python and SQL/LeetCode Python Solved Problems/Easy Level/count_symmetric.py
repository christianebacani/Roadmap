# 2843.) Count Symmetric Integers
# Categories: Math, Enumeration

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric_integers = []
        
        for i in range(low, high + 1):
            if len(str(i)) % 2 != 0:
                continue

            delimiter = len(str(i)) // 2
            
            first_half = str(i)[:delimiter]
            second_half = str(i)[delimiter:]
            
            first_half_sum = 0
            second_half_sum = 0
            
            for j in range(len(first_half)):
                first_half_sum += int(first_half[j])
            
            for j in range(len(second_half)):
                second_half_sum += int(second_half[j])

            if first_half_sum == second_half_sum:
                symmetric_integers.append(i)
        
        return len(symmetric_integers)
    
            

