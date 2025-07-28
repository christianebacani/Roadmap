# Question: Name on billboard
# Categories: 8 Kyu

def billboard(name, price=30) -> int:
    total = 0
    
    for _ in range(len(name)):
        total += price
    
    return total