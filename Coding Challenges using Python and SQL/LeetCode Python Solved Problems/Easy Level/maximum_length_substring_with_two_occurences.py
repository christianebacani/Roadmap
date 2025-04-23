# 3090.) Maximum Length Substring With Two Occurences
# Categories: Hash Table, String, Sliding Window

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        substrings = []

        for i in range(1, len(s) + 1):
            for j in range(len(s)):
                substring = s[j : j + i]
                letters_are_two_occurences_at_most = True

                for k in range(len(substring)):
                    if substring.count(substring[k]) > 2:
                       letters_are_two_occurences_at_most = False 
                       break
                
                if letters_are_two_occurences_at_most:
                    substrings.append(substring)

        maximum_length_of_substring = 0

        for i in range(len(substrings)):
            if len(substrings[i]) > maximum_length_of_substring:
                maximum_length_of_substring = len(substrings[i])
        
        return maximum_length_of_substring