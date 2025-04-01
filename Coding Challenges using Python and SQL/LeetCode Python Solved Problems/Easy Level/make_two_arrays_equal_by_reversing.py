# 1460.) Make Two Arrays Equal by Reversing
# Categories: Array, Hash Table, Sorting

class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        target = sorted(target)
        arr = sorted(arr)

        if target == arr:
            return True
        
        return False
    