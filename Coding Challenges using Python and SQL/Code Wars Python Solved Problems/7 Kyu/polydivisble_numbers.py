# Question: Polydivisible Numbers
# Categories: 7 Kyu

def polydivisible(number: int) -> bool:
    number_string = str(number)

    for i in range(1, len(number_string) + 1):
        if int(number_string[:i]) % i != 0:
            return False
    
    return True