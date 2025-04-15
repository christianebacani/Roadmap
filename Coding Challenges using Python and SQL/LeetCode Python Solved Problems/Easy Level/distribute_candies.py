# 575.) Distribute Candies
# Categories: Array, Hash Table

class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        number_of_candies_that_alice_can_eat = len(candyType) // 2
        distinct_number_of_different_types_of_candies = len(set(candyType))

        if distinct_number_of_different_types_of_candies > number_of_candies_that_alice_can_eat:
            return number_of_candies_that_alice_can_eat
        
        return distinct_number_of_different_types_of_candies