# 3541.) Find Most Frequent Vowel and Consonant
# Categories: Hash Table, String, Counting

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = 'aeiou'
        vowel_and_frequencies = {}
        consonant_and_frequencies = {}

        for i in range(len(s)):
            if s[i].lower() in vowels:
                vowel_and_frequencies[s[i]] = s.count(s[i])
            
            else:
                consonant_and_frequencies[s[i]] = s.count(s[i])
        
        answer = max(list(vowel_and_frequencies.values()), default=0) + max(list(consonant_and_frequencies.values()), default=0)

        return answer