# C - Clock Conversion

def convert_to_twelve_hour_format(time: str) -> str:
    time = time.split(':')
    hours = time[0]    
    minutes = time[1]    

    if int(hours) == 0:
        hours = '12'
        minutes = minutes
        meridiem = ' AM'
    
    elif int(hours) >= 1 and int(hours) <= 11:
        hours = hours
        minutes = minutes
        meridiem = ' AM'

    elif int(hours) == 12:
        hours = '12'
        minutes = minutes
        meridiem = ' PM'

    else:
        hours = str(int(hours) - 12)
        minutes = minutes
        meridiem = ' PM'
    
    if len(hours) != 2:
        hours = '0' + hours
    
    if len(minutes) != 2:
        minutes = '0' + minutes
    
    return hours + ':' + minutes + meridiem

t = int(input().strip())

for _ in range(t):
    print(convert_to_twelve_hour_format(input().strip()))