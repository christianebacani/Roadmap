# 1450.) Number of Students Doing Homework at a Given Time
# Categories: Array

class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        number_of_students = len(startTime)
        count = 0
    
        for i in range(number_of_students):
            start_time = startTime[i]
            end_time = endTime[i]
            
            if queryTime in range(start_time, end_time + 1):
                count += 1

        return count
    