# 3456.) Find Special Substring of Length K
# Categories: String

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(len(s)):
            substring = s[i : i + k]

            if len(substring) != k or len(set(substring)) != 1:
                continue

            if i - 1 < 0:
                character_before_the_substring = ' '
            
            else:
                character_before_the_substring = s[i - 1]
            
            if i + k > len(s) - 1:
                character_after_the_substring = ' '
            
            else:
                character_after_the_substring = s[i + k]


            if character_before_the_substring not in substring and character_after_the_substring not in substring:
                return True

        return False