# 2960.) Count Tested Devices After Test Operations
# Categories: Array, Simulation, Counting

class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        count = 0
        
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                count += 1
                
                for j in range(len(batteryPercentages)):
                    if (i < j) and (batteryPercentages[j] > 0):
                        batteryPercentages[j] -= 1
                
        return count
    