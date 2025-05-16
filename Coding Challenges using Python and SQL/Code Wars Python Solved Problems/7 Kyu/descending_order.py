# Question: Descending Order
# Categories: 7 Kyu

def descending_order(num: int) -> int:
    num = int(''.join(sorted(str(num), reverse=True)))

    return num