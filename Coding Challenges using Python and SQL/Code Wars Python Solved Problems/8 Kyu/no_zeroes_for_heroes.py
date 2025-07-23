# Question: No zeros for heroes
# Categorise: 8 Kyu

def no_boring_zeros(n: int) -> int:
    if n == 0:
        return n
    
    if not str(n).endswith('0'):
        return n

    n = list(str(n)[::-1])

    while True:
        if n[0] == '0':
            n = n[1:]
            continue

        break

    n = int(''.join(n[::-1]))
    return n