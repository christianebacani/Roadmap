# 2729.) Check if The Number is Fascinating
# Categories: Hash Table, Math

class Solution:
    def isFascinating(self, n: int) -> bool:
        n = str(n)
        n_multiply_by_2 = str(2 * int(n))
        n_multiply_by_3 = str(3 * int(n))

        concatenated_n = str(n + n_multiply_by_2 + n_multiply_by_3)

        for i in range(0, 10):
            if i == 0 and concatenated_n.count(str(i)) > 0:
                return False
            
            elif i != 0 and concatenated_n.count(str(i)) != 1:
                return False
        
        return True