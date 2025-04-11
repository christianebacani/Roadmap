# 3304.) Find the K-th Character in String Game I
# Categories: Math, Bit Manipulation, Recursion, Simulation

class Solution:
    def kthCharacter(self, k: int) -> str:
        alphabets = [
            'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
            'u', 'v', 'w', 'x',
            'y', 'z'
        ]
        word = 'a'
        
        while len(word) < k:
            lst = []
            
            for i in range(len(word)):
                if word[i] == 'z':
                    lst.append('a')
                    continue

                for j in range(len(alphabets)):
                    if word[i] == alphabets[j]:
                        lst.append(alphabets[j + 1])
            
            word = ''.join(lst)
            new_word = ''

            for i in range(len(word)):
                for j in range(len(alphabets)):
                    if word[i] == alphabets[j]:
                        new_word += alphabets[j - 1]
            
            word = new_word + word

        return word[k - 1]