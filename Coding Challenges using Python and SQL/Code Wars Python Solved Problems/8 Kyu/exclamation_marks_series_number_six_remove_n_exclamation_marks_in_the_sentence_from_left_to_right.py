# Question: Exclamation marks series #6: Remove n exclamation marks in the sentence from left to right
# Categories: 8 Kyu

def remove(st: str, n: int) -> str:
    result = ''
    frequency = 0

    for i in range(len(st)):
        if st[i] != '!':
            result += st[i]
            continue

        frequency += 1

        if frequency <= n:
            continue

        result += '!'
    
    return result