# 2848.) Points That Intersect with Cars
# Categories: Array, Hash Table, Prefix Sum

class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        integer_points = []

        for i in range(len(nums)):
            for j in range(nums[i][0], nums[i][1] + 1):
                integer_points.append(j)
        
        return len(set(integer_points))