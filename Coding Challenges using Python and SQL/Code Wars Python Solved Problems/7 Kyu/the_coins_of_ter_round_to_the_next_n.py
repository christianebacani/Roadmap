# Question: The Coins of Ter | Round to the Next N
# Categories: 7 Kyu

def adjust(coin: int, price: int) -> int:
    k = price

    while True:
        if (k >= price) and (k % coin == 0):
            break

        k += 1
    
    return k