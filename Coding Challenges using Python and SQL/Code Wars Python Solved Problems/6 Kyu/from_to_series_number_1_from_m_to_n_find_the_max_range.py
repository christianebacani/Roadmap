# Question: From..To..Series #1: from m to n. Find the maximum range
# Categories: 6 Kyu

def find_max_range(ranges: list[str]) -> list[str]:
    if ranges == []:
        return []

    maximum_distance = 0

    for i in range(len(ranges)):
        first_number = ranges[i].split('to')[0]
        first_number = first_number.replace('from', '')
        first_number = first_number.strip()
                        
        second_number = ranges[i].split('to')[1]
        second_number = second_number.strip()

        if '.' in first_number:
            first_number = float(first_number)
        
        else:
            first_number = int(first_number)
        
        if '.' in second_number:
            second_number = float(second_number)

        else:
            second_number = int(second_number)

        if abs(first_number - second_number) > maximum_distance:
            maximum_distance = abs(first_number - second_number)

    result = []
    
    for i in range(len(ranges)):
        first_number = ranges[i].split('to')[0]
        first_number = first_number.replace('from', '')
        first_number = first_number.strip()
                        
        second_number = ranges[i].split('to')[1]
        second_number = second_number.strip()

        if '.' in first_number:
            first_number = float(first_number)
        
        else:
            first_number = int(first_number)
        
        if '.' in second_number:
            second_number = float(second_number)

        else:
            second_number = int(second_number)

        if abs(first_number - second_number) == maximum_distance:
            result.append(ranges[i])

    return result