# Question: The Poet And The Pendulum
# Categories: 7 Kyu

def pendulum(values: list[int]) -> list[int]:
    values = sorted(values)
    result = [values[0]]
    values = values[1:]

    for i in range(len(values)):
        if i % 2 == 0:
            result.append(values[i])
        
        else:
            result.insert(0, values[i])
    
    return result