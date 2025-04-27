# 1629.) Slowest Key
# Categories: Array, String

class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        keys_and_total_duration = []
        
        for i in range(len(keysPressed)):
            if i == 0:
                keys_and_total_duration.append([keysPressed[i], releaseTimes[0]])
                continue

            keys_and_total_duration.append([keysPressed[i], releaseTimes[i] - releaseTimes[i - 1]])
        
        maximum_duration = 0

        for i in range(len(keys_and_total_duration)):
            duration = keys_and_total_duration[i][1]

            if duration > maximum_duration:
                maximum_duration = duration
        
        keys_with_maximum_duration = []

        for i in range(len(keys_and_total_duration)):
            key = keys_and_total_duration[i][0]
            duration = keys_and_total_duration[i][1]

            if duration == maximum_duration:
                keys_with_maximum_duration.append(key)
    
        return sorted(keys_with_maximum_duration, reverse=True)[0]
