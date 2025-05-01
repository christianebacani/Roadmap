# 1154.) Day of the Year
# Categories: Math, String

class Solution:
    def dayOfYear(self, date: str) -> int:
        def getTheTotalDaysOfMonth(year: str, month: str) -> int:
            month_and_total_days = {
                '01': 31, '02': 28, '03': 31,
                '04': 30, '05': 31, '06': 30,
                '07': 31, '08': 31, '09': 30,
                '10': 31, '11': 30, '12': 31
            }

            if int(year) % 400 == 0:
                month_and_total_days['02'] = 29
            
            if int(year) % 4 == 0 and int(year) % 100 != 0:
                month_and_total_days['02'] = 29

            if len(month) == 1:
                month = '0' + month

            return month_and_total_days[month]
        
        year = date[:4]
        month = date[5:7]
        day = date[-2:]

        total_days = 0

        if month == '01':
            total_days += int(day)

        else:
            for i in range(1, int(month)):
                total_days += getTheTotalDaysOfMonth(year, str(i))
        
            total_days += int(day)

        return total_days