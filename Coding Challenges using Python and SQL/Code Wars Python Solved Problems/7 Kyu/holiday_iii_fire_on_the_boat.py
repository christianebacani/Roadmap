# Question: Holiday III - Fire on the boat
# Categories: 7 Kyu

def fire_fight(s: str) -> str:
    s = s.split()
    
    for i in range(len(s)):
        if s[i] == 'Fire':
            s[i] = '~~'
        
        else:
            pass
    
    s = ' '.join(s)
    return s