# 2869.) Minimum Operations to Collect Elements
# Categories: Array, Hash Table, Bit Manipulation

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        collected_elements = []
        
        while True:
            collected_elements.append(nums[-1])
            nums.pop(-1)
            
            is_collected_all_elements = True

            for i in range(1, k + 1):
                if i not in collected_elements:
                    is_collected_all_elements = False
                    break
            
            if is_collected_all_elements:
                break

        return len(collected_elements)