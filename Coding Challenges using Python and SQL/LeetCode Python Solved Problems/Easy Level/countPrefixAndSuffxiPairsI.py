# 3042.) Count Prefix and Suffix Pairs I
# Categories: Array, String, Trie, Rolling Hash, String Matching, Hash Function

class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            if str2.startswith(str1) and str2.endswith(str1):
                return True
            
            return False
        
        index_pairs = []
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i < j and isPrefixAndSuffix(words[i], words[j]):
                    index_pairs.append(tuple([i, j]))
        
        return len(index_pairs)
