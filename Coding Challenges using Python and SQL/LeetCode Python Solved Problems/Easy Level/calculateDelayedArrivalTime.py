# 2651.) Calculate Delayed Arrival Time
# Categories: Math

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        if (arrivalTime + delayedTime) >= 24:
            return (arrivalTime + delayedTime) - 24
        
        return arrivalTime + delayedTime