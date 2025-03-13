# 1688.) Count of Matches in Tournament
# Categories: Math, Simulation

class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches = 0

        while True:
            if n % 2 == 0:
                matches = n // 2
                total_matches += matches
                n = n // 2

            else:
                matches = (n - 1) // 2
                total_matches += matches
                n = ((n - 1) // 2) + 1
        
            if n == 1:
                return int(total_matches)
