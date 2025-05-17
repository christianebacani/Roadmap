# Question: Credit Card Mask
# Categories: 7 Kyu

def maskify(cc: str) -> str:
    if len(cc) <= 4:
        return cc
    
    last_four_characters = cc[-4:]
    cc = list(cc[:-4])

    for i in range(len(cc)):
        cc[i] = '#'
    
    cc = ''.join(cc) + last_four_characters

    return cc