# 2399.) Check Distances Between Same Letters
# Categories: Array, Hash Table, String

class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        alphabets = [
            'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
            'u', 'v', 'w', 'x',
            'y', 'z'
        ]
        letter_distances = {}

        for i in range(len(s)):
            if s[i] in letter_distances:
                continue
        
            substring = [s[i]]

            for j in range(len(s[i + 1:])):
                if s[i + 1:][j] == s[i]:
                    substring.append(s[i + 1:][j])
                    break

                else:
                    substring.append(s[i + 1:][j])
    
            letter_distances[s[i]] = len(substring[1:-1])
        
        for letter, distances in letter_distances.items():
            if distance[alphabets.index(letter)] != distances:
                return False

        return True