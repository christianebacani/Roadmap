# 2600.) K Items With the Maxium Sum
# Categories: Math, Greedy

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        items = []

        for _ in range(numOnes):
            items.append(1)
        
        for _ in range(numZeros):
            items.append(0)
        
        for _ in range(numNegOnes):
            items.append(-1)
        
        return sum(items[:k])