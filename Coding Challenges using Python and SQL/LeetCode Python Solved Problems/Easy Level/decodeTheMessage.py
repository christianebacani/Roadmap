# 2325.) Decode the Message
# Categories: Hash Table, String

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabets = ['a', 'b', 'c', 'd', 'e',
                 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o',
                 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    
        distinct_key = []
        key_with_alphabets = {}
        decoded_message = ''

        for i in range(len(key)):
            if key[i] not in distinct_key and key[i] != ' ':
                distinct_key.append(key[i])
    
        for i in range(len(distinct_key)):
            for j in range(len(alphabets)):
                if i == j:
                    key_with_alphabets[distinct_key[i]] = alphabets[j]
    
        for char in message:
            if char == ' ':
                decoded_message += ' '
        
            else:
                decoded_message += key_with_alphabets[char]
    
        return decoded_message
