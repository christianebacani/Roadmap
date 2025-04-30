# 2432.) The Employee That Worked on the Longest Task
# Categories: Array

from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        maximum_time_to_finish_task = 0

        for i in range(len(logs)):
            if i == 0 and logs[i][1] > maximum_time_to_finish_task:
                maximum_time_to_finish_task = logs[i][1]
            
            elif i != 0 and logs[i][1] - logs[i - 1][1] > maximum_time_to_finish_task:
                maximum_time_to_finish_task = logs[i][1] - logs[i - 1][1]
                        
        employee_id_who_worked_the_most_time = []

        for i in range(len(logs)):
            if i == 0 and logs[i][1] == maximum_time_to_finish_task:
                employee_id_who_worked_the_most_time.append(logs[i][0])
            
            elif i != 0 and logs[i][1] - logs[i - 1][1] == maximum_time_to_finish_task:
                employee_id_who_worked_the_most_time.append(logs[i][0])
        
        return min(employee_id_who_worked_the_most_time)