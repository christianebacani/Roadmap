# 3536.) Maximum Product of Two Digits
# Categories: Math, Sorting

class Solution:
    def maxProduct(self, n: int) -> int:
        n = sorted(str(n), reverse=True)

        return int(n[0]) * int(n[1])