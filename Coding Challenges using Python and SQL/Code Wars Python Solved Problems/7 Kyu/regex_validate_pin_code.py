# Question: Regex validate PIN code
# Categories: 7 Kyu

def validate_pin(pin: str) -> bool:
    count = 0

    for i in range(len(pin)):
        if not pin[i].isnumeric():
            return False

        if pin[i].isnumeric():
            count += 1
    
    return count == 4 or count == 6