# 3442.) Maximum Difference Between Even and Odd Frequency I
# Categories: Hash Table, String, Counting

class Solution:
    def maxDifference(self, s: str) -> int:
        character_and_frequency = {}

        for i in range(len(s)):
            character_and_frequency[s[i]] = s.count(s[i])

        sorted_in_maximum_frequency = sorted(list(character_and_frequency.values()), reverse=True)
        sorted_in_minimum_frequency = sorted(list(character_and_frequency.values()))

        for i in range(len(sorted_in_maximum_frequency)):
            if sorted_in_maximum_frequency[i] % 2 != 0:
                maximum_odd_frequency = sorted_in_maximum_frequency[i]
                break
        
        for i in range(len(sorted_in_minimum_frequency)):
            if sorted_in_minimum_frequency[i] % 2 == 0:
                minimum_even_frequency = sorted_in_minimum_frequency[i]
                break
        
        return maximum_odd_frequency - minimum_even_frequency