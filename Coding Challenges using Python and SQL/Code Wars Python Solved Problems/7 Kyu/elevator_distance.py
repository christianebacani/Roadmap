# Question: Elevator Distance
# Categories: 7 Kyu

def elevator_distance(array: list[int]) -> int:
    distances = []

    for i in range(1, len(array)):
        previous_floor = array[i - 1]
        current_floor = array[i]

        distances.append(abs(previous_floor - current_floor))
    
    return sum(distances)