# Question: From-To-Step Sequence Generator
# Categories: 7 Kyu

def generator (start: int, stop: int, step: int) -> list[int]:
    result = []

    try:
        if stop > start:
            for i in range(start, stop + 1, step):
                result.append(i)
        
        for i in range(start, stop - 1, step * -1):
            result.append(i)

    except:
        pass

    return result