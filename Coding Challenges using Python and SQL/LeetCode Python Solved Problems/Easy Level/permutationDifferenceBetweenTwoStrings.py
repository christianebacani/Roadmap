# 3146.) Permutation Difference between Two Strings
# Categories : Hash Table, String

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum_abs_diff = 0

        for char in s:
            for index, inner_char in enumerate(s):
                if char == inner_char:
                    s_index = index

            for index, inner_char in enumerate(t):
                if char == inner_char:
                    t_index = index

            sum_abs_diff += abs(s_index - t_index)

        return sum_abs_diff
