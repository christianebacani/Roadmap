# 2951.) Find the Peaks
# Categories: Array, Enumeration

class Solution:
    def findPeaks(self, mountain: list[int]) -> list[int]:
        first_mountain_index = 0
        last_mountain_index = len(mountain) - 1
        peak_mountain_indices = []

        for i in range(len(mountain)):
            if (i == first_mountain_index) or (i == last_mountain_index):
                continue
            
            if (mountain[i] > mountain[i - 1]) and (mountain[i] > mountain[i + 1]):
                peak_mountain_indices.append(i)
            
        return peak_mountain_indices