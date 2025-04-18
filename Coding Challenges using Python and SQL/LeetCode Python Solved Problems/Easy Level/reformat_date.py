# 1507.) Reformat Date
# Categories: String

class Solution:
    def reformatDate(self, date: str) -> str:
        ordinal_num_suffix = ['st', 'nd', 'rd', 'th']
        day = date.split()[0]

        for i in range(len(ordinal_num_suffix)):
            day = day.replace(ordinal_num_suffix[i], '')
        
        if len(day) != 2:
            day = '0' + day

        month_to_integer = {
            'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
            'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
            'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
        }

        month = month_to_integer[date.split()[1].capitalize()]
        year = date.split()[2]

        return f'{year}-{month}-{day}'