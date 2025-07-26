# Question: Sum of numbers from 0 to N
# Categories: 7 Kyu

def show_sequence(n: int) -> str:
    if n == 0:
        return '0=0'
    
    elif n < 0:
        return f'{n}<0'
    
    else:
        result = []
        
        for number in range(n + 1):
            result.append(str(number))
        
        total = 0

        for i in range(len(result)):
            total += int(result[i])

        result = '+'.join(result)
        result = result + ' = ' + str(total)

        return result