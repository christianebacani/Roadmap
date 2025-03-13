# 1313.) Decompress Run-Length Encoded List
# Categories: Array

class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        decompressed_list = []

        for i in range(0, len(nums), 2):
            pair = [nums[i], nums[i + 1]]

            for j in range(pair[0]):
                decompressed_list.append(pair[1])
    
        return decompressed_list
