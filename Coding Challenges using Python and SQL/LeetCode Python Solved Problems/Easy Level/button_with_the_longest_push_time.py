# 3386.) Button with Longest Push Time
# Categories: Array

from typing import List

class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        maximum_time_to_push_the_button = 0

        for i in range(len(events)):
            if i == 0 and events[i][1] > maximum_time_to_push_the_button:
                maximum_time_to_push_the_button = events[i][1]

            elif i != 0 and events[i][1] - events[i - 1][1] > maximum_time_to_push_the_button:
                maximum_time_to_push_the_button = events[i][1] - events[i - 1][1]

        indices_of_maximum_time = []

        for i in range(len(events)):
            if i == 0 and events[i][1] == maximum_time_to_push_the_button:
               indices_of_maximum_time.append(events[i][0])

            elif i != 0 and events[i][1] - events[i - 1][1] == maximum_time_to_push_the_button:
                indices_of_maximum_time.append(events[i][0])
        
        return min(indices_of_maximum_time)