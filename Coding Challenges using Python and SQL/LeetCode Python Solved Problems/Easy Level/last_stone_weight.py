# 1046.) Last Stone Weight
# Categories: Array, Heap (Priority Queue)

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones, reverse=True)
            first_max_num = stones[0]
            second_max_num = stones[1]

            stones = stones[2:]
            
            if first_max_num != second_max_num:
                stones.append(abs(first_max_num - second_max_num))

        if stones == []:
            return 0
    
        return stones[0]
