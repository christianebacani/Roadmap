# Questio: Persistence Bugger
# Categories: 6 Kyu

def persistence(n: int):
    count = 0
    
    while len(str(n)) != 1:
        count += 1
        result = 1

        for i in range(len(str(n))):
            result *= int(str(n)[i])
        
        n = result

    return count