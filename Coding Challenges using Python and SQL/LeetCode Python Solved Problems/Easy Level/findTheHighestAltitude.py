# 1732.) Find the Highest Altitude
# Categories: Array, Prefix Sum

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitudes = [0]

        for i in range(len(gain)):
            altitudes.append(altitudes[-1] + gain[i])
    
        return max(altitudes)