# 599.) Minimum Index Sum of Two Lists
# Categories: Array, Hash Table, String

from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_string_and_index_sum = {}

        for i in range(len(list1)):
            if list1[i] in list2:
                common_string_and_index_sum[list1[i]] = i + list2.index(list1[i])
        
        minimum_index_sum = min(list(common_string_and_index_sum.values()))
        common_string_with_min_index_sum = []
        
        for string, index_sum in common_string_and_index_sum.items():
            if minimum_index_sum == index_sum:
                common_string_with_min_index_sum.append(string)
        
        return common_string_with_min_index_sum