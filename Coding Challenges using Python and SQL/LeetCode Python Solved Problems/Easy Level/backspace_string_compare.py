# 844.) Backspace String Compare
# Categories: Two Pointers, String, Stack, Simulation

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_after_performing_backspace = []
        t_after_performing_backspace = []

        for i in range(len(s)):
            if s[i] != '#':
                s_after_performing_backspace.append(s[i])

            else:
                s_after_performing_backspace = s_after_performing_backspace[:-1]

        for i in range(len(t)):
            if t[i] != '#':
                t_after_performing_backspace.append(t[i])

            else:
                t_after_performing_backspace = t_after_performing_backspace[:-1]

        if ''.join(s_after_performing_backspace) == ''.join(t_after_performing_backspace):
            return True
        
        return False