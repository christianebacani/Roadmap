# 1408.) String Matching in an Array
# Categories: Array, String, String Matching

class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        matched_strings = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    matched_strings.append(words[i])
                    break
        
        return matched_strings