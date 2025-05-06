# 2744.) Find Maximum Number of String Pairs
# Categories: Array, Hash Table, String, Simulation

from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        number_of_string_pairs = 0

        for i in range(len(words)):
            for j in range(len(words)):
                if i < j and words[i] == words[j][::-1]:
                    number_of_string_pairs += 1
        
        return number_of_string_pairs