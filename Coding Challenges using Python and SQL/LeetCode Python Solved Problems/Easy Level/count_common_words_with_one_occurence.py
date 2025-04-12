# 2085.) Count Common Words With One Occurence
# Categories: Array, Hash Table, String, Counting

class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        count = 0
        
        for i in range(len(words1)):
            word1_count = words1.count(words1[i])
            word2_count = words2.count(words1[i])

            if word1_count == word2_count == 1:
                count += 1
            
        return count