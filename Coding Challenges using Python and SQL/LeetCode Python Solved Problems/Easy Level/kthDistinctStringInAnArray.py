# 2053.) Kth Distinct String in an Array
# Categories: Array, Hash Table, String, Counting

class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        distinct_elements = []
        
        for i in range(len(arr)):
            count = 0
            
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    count += 1
            
            if count == 1:
                distinct_elements.append(arr[i])

        if len(distinct_elements) < k:
            return ""
        
        return distinct_elements[k - 1]
    