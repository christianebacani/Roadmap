# Question: Take a Ten Minutes Walk
# Categories: 6 Kyu

def is_valid_walk(walk):
    current_location = [0, 0]
    total_minutes = 0

    for i in range(len(walk)):
        if walk[i] == 'n':
            current_location[1] += 1
            total_minutes += 1

        elif walk[i] == 's':
            current_location[1] -= 1
            total_minutes += 1

        elif walk[i] == 'w':
            current_location[0] -= 1
            total_minutes += 1
        
        else:
            current_location[0] += 1
            total_minutes += 1
    
    if current_location == [0, 0] and total_minutes == 10:
        return True
    
    return False