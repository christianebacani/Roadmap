# 1941.) Check if All Characters Have Equal Number of Occurences
# Categories: Hash Table, String, Counting

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        character_frequencies = {}
        
        for i in range(len(s)):
            frequency = 0
            
            for j in range(len(s)):
                if s[i] == s[j]:
                    frequency += 1
            
            character_frequencies[s[i]] = frequency
        
        frequencies = list(character_frequencies.values())

        for i in range(1, len(frequencies)):
            if frequencies[i] != frequencies[i - 1]:
                return False
        
        return True
        