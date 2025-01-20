# 14.) Longest Common Prefix
# Category : String, Trie

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        possiblePrefixes = []
        for i in range(len(strs[0])):
            word = strs[0][:i+1]
            possiblePrefixes.append(word)

        commonPrefixes = []
        for prefix in possiblePrefixes:
            for word in strs:
                if word.startswith(prefix):
                    commonPrefix = prefix
            
                else:
                    commonPrefix = ''
                    break

            commonPrefixes.append(commonPrefix)
    

        largestCommonPrefix = ''
        for prefix in commonPrefixes:
            if len(prefix) > len(largestCommonPrefix):
                largestCommonPrefix = prefix
        
            else:
                pass
    
        return largestCommonPrefix

