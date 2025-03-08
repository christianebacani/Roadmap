# 2798.) Number of Employees Who Met the Target
# Categories: Array

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        count = 0

        for i in range(len(hours)):
            if hours[i] >= target:
                count += 1
    
        return count
