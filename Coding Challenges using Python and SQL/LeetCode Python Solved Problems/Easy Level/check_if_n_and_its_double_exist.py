# 1346.) Check if N and Its Double Exist
# Categories: Array, Hash Table, Two Pointers, Binary Search, Sorting

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    continue

                if arr[i] == (arr[j] * 2):
                    return True
        
        return False