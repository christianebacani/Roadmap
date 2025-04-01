# 2558.) Take Gifts From the Richest Pile
# Categories: Array, Heap(Priority Queue), Simulation

import math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        for i in range(k):
            maximum_number_of_gifts = max(gifts)
            number_of_gifts = math.floor(math.sqrt(maximum_number_of_gifts))

            gifts = sorted(gifts, reverse=True)
            gifts[0] = number_of_gifts
        
        return sum(gifts)
