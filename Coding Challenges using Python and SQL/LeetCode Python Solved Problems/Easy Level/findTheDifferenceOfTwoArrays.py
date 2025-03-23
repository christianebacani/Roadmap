# 2215.) Find the Difference of Two Arrays
# Categories: Array, Hash Table

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer = [[], []]
        
        distinct_nums1_integers =  list(set(nums1))
        distinct_nums2_integers = list(set(nums2))
        
        for distinct_num1 in distinct_nums1_integers:
            if distinct_num1 not in distinct_nums2_integers:
                answer[0].append(distinct_num1)
        
        for distinct_num2 in distinct_nums2_integers:
            if distinct_num2 not in distinct_nums1_integers:
                answer[1].append(distinct_num2)
        
        return answer
