# Question: Mirror, mirror, on the wall...
# Categories: 7 Kyu

def mirror(data: list) -> list:
    if data == []:
        return []

    data = sorted(data, reverse=True)
    result = []

    result.append(data[0])
    data = data[1:]

    for i in range(len(data)):
        result.insert(0, data[i])
        result.append(data[i])
    
    return result