# Question: Does my number look big in this?
# Categories: 6 Kyu

def narcissistic(value: int) -> bool:
    value = str(value)
    power = len(value)

    total = 0

    for i in range(len(value)):
        total += (int(value[i]) ** power)
    
    if total == int(value):
        return True
    
    return False