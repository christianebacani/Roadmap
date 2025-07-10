# Question: Borrower Speak
# Categories: 7 Kyu

def borrow(s: str) -> str:
    s = s.split()
    punctuations = '.?,!"":;\''
    result = ''
    
    for i in range(len(s)):
        for j in range(len(punctuations)):
            if punctuations[j] in s[i]:
                s[i] = s[i].replace(punctuations[j], '')
        
        s[i] = s[i].lower()
        result += s[i]
    
    return result