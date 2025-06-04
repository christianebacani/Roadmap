# Question: Time Converter: hours, minutes, seconds and milliseconds
# Categories: 7 Kyu

from datetime import datetime

def convert(time: datetime) -> str:
    time = str(time).split()[1]

    if '.' not in time:
        return time + ',000'

    milliseconds = str(time).split('.')[1][:3]
    return str(time).split('.')[0] + ',' + milliseconds