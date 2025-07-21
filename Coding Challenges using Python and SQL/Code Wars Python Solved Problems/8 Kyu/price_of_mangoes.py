# Question: Price of Mangoes
# Categories: 8 Kyu

def mango(quantity: int, price: int) -> int:
    total_price = 0

    while quantity > 0:
        if quantity % 3 == 0:
            pass

        else:
            total_price += price

        quantity -= 1

    return total_price