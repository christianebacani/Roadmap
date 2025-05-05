# 3271.) Hash Divided String
# Categories: String, Simulation

class Solution:
    def stringHash(self, s: str, k: int) -> str:
        alphabets = [
            'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
            'u', 'v', 'w', 'x',
            'y', 'z'
        ]
        substrings = []

        for i in range(0, len(s), k):
            substring = s[i : i + k]

            if len(substring) != k:
                continue
        
            substrings.append(substring)
        
        result = ''

        for i in range(len(substrings)):
            total_hash_value = 0

            for j in range(len(substrings[i])):
                total_hash_value += alphabets.index(substrings[i][j])
            
            result += alphabets[total_hash_value % 26]

        return result