# 3492.) Maximum Containers on a Ship
# Categories: Math

class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        cell = n * n
        total_weight = 0
        count = 0

        for _ in range(cell):
            total_weight += w 

            if total_weight > maxWeight:
                break
            
            count += 1

        return count
