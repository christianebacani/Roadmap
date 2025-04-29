# 2446.) Determine if Two Events Have Conflict
# Categories: Array, String

from typing import List

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def convertTimeToMinutes(time: str) -> int:
            hour = int(time[:2])
            minutes = int(time[3:])

            return (hour * 60) + minutes

        event1_minutes_started = convertTimeToMinutes(event1[0])
        event1_minutes_ended = convertTimeToMinutes(event1[1])

        event2_minutes_started = convertTimeToMinutes(event2[0])
        event2_minutes_ended = convertTimeToMinutes(event2[1])

        for i in range(event1_minutes_started, event1_minutes_ended + 1):
            if i in range(event2_minutes_started, event2_minutes_ended + 1):
                return True

        return False