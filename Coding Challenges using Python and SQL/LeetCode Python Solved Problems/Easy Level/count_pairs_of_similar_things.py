# 2506.) Count Pairs of Similar Things
# Categories: Array, Hash Table, String, Bit Manipulation, Counting

class Solution:
    def similarPairs(self, words: list[str]) -> int:
        count = 0
    
        for i in range(len(words)):
            words[i] = sorted(set(words[i]))

            for j in range(len(words)):
                words[j] = sorted(set(words[j]))

                if (i < j) and (words[i] == words[j]):
                    count += 1
        
        return count