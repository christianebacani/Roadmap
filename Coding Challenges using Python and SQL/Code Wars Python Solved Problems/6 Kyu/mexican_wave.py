# Question: Mexican Wave
# Categories: 6 Kyu

def wave(people: str) -> list[str]:
    result = []

    for i in range(len(people)):
        if people[i].isalpha():
            wave_result = people[:i] + people[i].upper() + people[i + 1:]
            result.append(wave_result)

    return result