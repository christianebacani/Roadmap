# 551.) Student Attendance Record I
# Categories: String

class Solution:
    def checkRecord(self, s: str) -> bool:
        number_of_absent_days = s.count('A')
        student_late_for_3_or_more_cons_days = False
        
        if 'LLL' in s:
            student_late_for_3_or_more_cons_days = True
        
        if number_of_absent_days <= 1 and not student_late_for_3_or_more_cons_days:
            return True
        
        return False