# 1281.) Subtract the Product and Sum of Digits of an Integer
# Categories: Math

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        total_product = int(n[0])
        total_sum = int(n[0])
    
        for i in range(1, len(n)):
            total_product *= int(n[i])
            total_sum += int(n[i])

        return total_product - total_sum
