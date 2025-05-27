# Question: Ciphers #1 - The 01 Cipher
# Categories: 7 Kyu

def encode(s: str) -> str:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for i in range(len(s)):
        if not s[i].isalpha():
            result += s[i]
            continue

        if alphabets.index(s[i].lower()) % 2 == 0:
            result += '0'
        
        else:
            result += '1'
    
    return result