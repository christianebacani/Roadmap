# 821.) Shortest Distance to a Character
# Categories: Array, Two Pointers, String

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        indices_of_c = []

        for i in range(len(s)):
            if s[i] == c:
                indices_of_c.append(i)
        
        answer = []

        for i in range(len(s)):
            if s[i] == c:
                answer.append(0)
                continue

            distances = []

            for j in range(len(indices_of_c)):
                distances.append(abs(indices_of_c[j] - i))
            
            answer.append(min(distances))
        
        return answer
    