# 2570.) Merge Two 2D Arrays by Summing Values
# Categories : Array, Hash Table, Two Pointers

class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        nums1_dict = dict(nums1)
        nums2_dict = dict(nums2)
        merged_nums_dict = {}

        for nums1_id, nums1_value in nums1_dict.items():
            for nums2_id, nums2_value in nums2_dict.items():
                if (nums1_id == nums2_id):
                    sum_value = nums1_value + nums2_value
                    merged_nums_dict[nums1_id] = sum_value

    
        for nums1_id, nums1_value in nums1_dict.items():
            if nums1_id not in merged_nums_dict:
                merged_nums_dict[nums1_id] = nums1_value
    
        for nums2_id, nums2_value in nums2_dict.items():
            if nums2_id not in merged_nums_dict:
                merged_nums_dict[nums2_id] = nums2_value
    
    
        sorted_merge_ids = sorted(list(merged_nums_dict.keys()))
        merged_nums = []
    

        for sorted_merge_id in sorted_merge_ids:
            for merge_id, merge_value in merged_nums_dict.items():
                if (sorted_merge_id == merge_id):
                    merged_nums.append([sorted_merge_id, merge_value])
    
        return merged_nums