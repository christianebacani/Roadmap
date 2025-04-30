# 125.) Valid Palindrome
# Categories: Two Pointers, String

class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted_string = []

        for i in range(len(s)):
            if s[i].isalnum():
                converted_string.append(s[i].lower())
            
            continue
        
        if ''.join(converted_string) == ''.join(converted_string)[::-1]:
            return True
        
        return False