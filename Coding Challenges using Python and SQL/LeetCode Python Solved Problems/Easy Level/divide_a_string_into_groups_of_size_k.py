# 2138.) Divide a String Into Groups of Size K
# Categories: String, Simulation

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        result = []

        for i in range(0, len(s), k):
            substring = s[i:i + k]

            if len(substring) == k:
                result.append(substring)
                continue

            substring = substring + ((k - len(substring)) * fill)
            result.append(substring)
        
        return result