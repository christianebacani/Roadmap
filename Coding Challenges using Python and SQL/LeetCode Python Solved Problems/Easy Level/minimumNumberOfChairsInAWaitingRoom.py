# 3168.) Minimum Number of Chairs in a Waiting Room
# Categories: String, Simulation

class Solution:
    def minimumChairs(self, s: str) -> int:
        number_of_chairs_needed = []
        number_of_chairs = 0
        
        for i in range(len(s)):
            if s[i] == 'E':
                number_of_chairs += 1
                number_of_chairs_needed.append(number_of_chairs)

            else:
                number_of_chairs -= 1
        
        return max(number_of_chairs_needed)