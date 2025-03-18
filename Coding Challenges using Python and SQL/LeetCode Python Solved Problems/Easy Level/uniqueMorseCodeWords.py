# 804.) Unique Morse Code Words
# Categories: Array, Hash Table, String

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_codes = {
            'a': ".-", 'b': "-...", 'c': "-.-.",
            'd': "-..", 'e': ".", 'f': "..-.",
            'g': "--.", 'h': "....", 'i': "..",
            'j': ".---", 'k': "-.-", 'l': ".-..",
            'm': "--", 'n': "-.", 'o': "---", 
            'p': ".--.", 'q': "--.-",'r': ".-.", 
            's': "...", 't': "-", 'u': "..-", 
            'v': "...-", 'w': ".--", 'x': "-..-", 
            'y': "-.--", 'z': "--.."
        }
        unique_encoded_morse_codes = []
    
        for i in range(len(words)):
            encoded_morse_code = ''
    
            for j in range(len(words[i])):
                encoded_morse_code += morse_codes[words[i][j]]
        
            if encoded_morse_code not in unique_encoded_morse_codes:
                unique_encoded_morse_codes.append(encoded_morse_code)
    
        return len(unique_encoded_morse_codes)
