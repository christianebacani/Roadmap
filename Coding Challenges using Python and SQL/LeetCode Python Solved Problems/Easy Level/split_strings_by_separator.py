# 2788.) Split Strings by Separator
# Categories: Array, String

class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        result = []
        
        for i in range(len(words)):
            splitted_word = words[i].split(separator)
            
            for j in range(len(splitted_word)):
                if splitted_word[j] != '':
                    result.append(splitted_word[j])
        
        return result
            