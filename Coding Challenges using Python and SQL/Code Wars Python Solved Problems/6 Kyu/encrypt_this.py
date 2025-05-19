# Question: Encrypt this!
# Categories: 6 Kyu

def encrypt_this(text: str) -> str:
    text = text.split()
    encrypted_text = []
    
    for i in range(len(text)):
        word = list(text[i])
        encrypted_word = []

        for j in range(len(word)):
            if j == 0:
                encrypted_word.append(str(ord(word[j])))
            
            elif j == 1:
                encrypted_word.append(word[-1])
            
            elif j == len(word) - 1:
                encrypted_word.append(word[1])
            
            else:
                encrypted_word.append(word[j])
        
        encrypted_text.append(''.join(encrypted_word))
    
    return ' '.join(encrypted_text)