# 1929.) Concatenation of Array
# Categories : Array, Simulation

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        second_nums = nums
        ans = nums + second_nums
        return ans