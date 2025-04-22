# 796.) Rotate String
# Categories: String, String Matching

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i = 0
        
        while i < len(s):
            if s == goal:
                return True
            
            s = s[1:] + s[0]
            i += 1

        return False