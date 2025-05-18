# Question: Make the Deadfish Swim
# Categories: 6 Kyu

def parse(data: str) -> list[int]:
    result = []
    value = 0

    for i in range(len(data)):
        if data[i] == 'i':
            value += 1
        
        elif data[i] == 'd':
            value -= 1
        
        elif data[i] == 's':
            value = value ** 2
        
        elif data[i] == 'o':
            result.append(value)

        else:
            pass

    return result