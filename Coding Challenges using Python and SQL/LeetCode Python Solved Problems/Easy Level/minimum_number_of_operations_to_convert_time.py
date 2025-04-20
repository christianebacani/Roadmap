# 2224.) Minimum Number of Operations to Convert Time
# Categories: String, Greedy

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def convertTimeToMinutes(time: str) -> int:
            hour = int(time[:2])
            minutes = int(time[3:])

            return (hour * 60) + minutes
        
        current_minutes = convertTimeToMinutes(current)
        correct_minutes = convertTimeToMinutes(correct)
        minutes_gap = correct_minutes - current_minutes
        
        number_of_operations = 0

        while minutes_gap != 0:
            minutes_increased = [60, 15, 5, 1]

            for i in range(len(minutes_increased)):
                if minutes_gap >= minutes_increased[i]:
                    number_of_operations += (minutes_gap // minutes_increased[i])
                    minutes_gap = minutes_gap - ((minutes_gap // minutes_increased[i]) * minutes_increased[i])

        return number_of_operations