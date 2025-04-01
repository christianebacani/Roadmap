# 884.) Uncommon Words from Two Sentences
# Categories: Hash Table, String, Counting

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        uncommon_words = []
        s1 = s1.split()
        s2 = s2.split()

        for i in range(len(s1)):
            frequency = s1.count(s1[i])
            
            if (frequency == 1) and (s1[i] not in s2):
                uncommon_words.append(s1[i])
        
        for i in range(len(s2)):
            frequency = s2.count(s2[i])

            if (frequency == 1) and (s2[i] not in s1):
                uncommon_words.append(s2[i])

        return uncommon_words
 