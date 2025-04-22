# 383.) Ransom Note
# Categories: Hash Table, String, Counting

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            if ransomNote.count(ransomNote[i]) > magazine.count(ransomNote[i]):
                return False
        
        return True