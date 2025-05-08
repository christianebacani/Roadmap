# 2206.) Divide Array Into Equal Pairs
# Categories: Array, Hash Table, Bit Manipulation, Counting

from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        number_of_pairs = len(nums) // 2
        pairs = []

        for _ in range(number_of_pairs):
            pair = []

            pair.append(nums[0])
            nums = nums[1:]

            for j in range(len(nums)):
                if nums[j] == pair[-1]:
                    pair.append(nums[j])
                    nums = nums[:j] + nums[j + 1:]
                    break
            
            if len(pair) != 2:
                return False

            pairs.append(pair)

        if len(pairs) != number_of_pairs:
            return False

        return True