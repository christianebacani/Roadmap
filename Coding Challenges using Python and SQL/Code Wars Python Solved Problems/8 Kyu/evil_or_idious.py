# Question: Evil or Odious
# Categories: 8 Kyu

def evil(n: int) -> str:
    binary_of_n = bin(n)[2:]
    
    if binary_of_n.count('1') % 2 == 0:
        return 'It\'s Evil!'
    
    return 'It\'s Odious!'