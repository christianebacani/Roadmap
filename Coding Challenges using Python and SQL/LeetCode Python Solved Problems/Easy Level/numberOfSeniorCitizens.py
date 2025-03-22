# 2678.) Number of Senior Citizens
# Categories: Array, String

class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count = 0

        for i in range(len(details)):
            age_of_passenger = int(''.join(details[i][11:13]))
            
            if age_of_passenger > 60:
                count += 1

        return count
        
        