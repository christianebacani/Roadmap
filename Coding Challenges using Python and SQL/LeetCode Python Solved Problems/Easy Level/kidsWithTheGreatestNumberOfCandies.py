# 1431.) Kids With the Greatest Number of Candies
# Categories : Array

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maximum_number_of_candies = max(candies)
        result = []

        for candy in candies:
            total_number_of_candies = candy + extraCandies

            if total_number_of_candies >= maximum_number_of_candies:
                result.append(True)
        
            else:
                result.append(False)
    
        return result
