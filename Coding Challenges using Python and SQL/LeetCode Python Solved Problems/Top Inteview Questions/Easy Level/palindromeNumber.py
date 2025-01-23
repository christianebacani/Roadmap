# 9.) Palindrome Number
# Category : Math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)

        if str(x) == string[::-1]:
            return True
        return False