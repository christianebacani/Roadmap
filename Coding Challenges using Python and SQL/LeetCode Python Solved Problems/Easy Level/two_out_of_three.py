# 2032.) Two Out of Three
# Categories: Array, Hash Table, Bit Manipulation

class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        nums = list(set(nums1 + nums2 + nums3))
        result = []
        
        for i in range(len(nums)):
            count = 0
            
            for j in range(len(nums1)):
                if nums[i] == nums1[j]:
                    count += 1
                    break
                
            for j in range(len(nums2)):
                if nums[i] == nums2[j]:
                    count += 1
                    break

            for j in range(len(nums3)):
                if nums[i] == nums3[j]:
                    count += 1
                    break
            
            if count > 1:
                result.append(nums[i])

        return result        
            
            