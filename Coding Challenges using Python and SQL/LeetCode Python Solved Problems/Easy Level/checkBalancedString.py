# 3340.) Check Balanced String
# Categories: String

class Solution:
    def isBalanced(self, num: str) -> bool:
        sum_of_even_indices = 0
        sum_of_odd_indices = 0
    
        for i in range(len(num)):
            if i % 2 == 0:
                sum_of_even_indices += int(num[i])

            else:
                sum_of_odd_indices += int(num[i])

        if sum_of_even_indices == sum_of_odd_indices:
            return True
    
        return False

