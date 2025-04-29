# 3477.) Fruits Into Baskets II
# Categories: Array, Binary Search, Segment Tree, Simulation

from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        number_of_unplaced_fruits = 0

        for i in range(len(fruits)):
            fruits_are_placed_to_the_basket = False

            for j in range(len(baskets)):
                if baskets[j] >= fruits[i]:
                    fruits_are_placed_to_the_basket = True
                    baskets.pop(j)
                    break
            
            if not fruits_are_placed_to_the_basket:
                number_of_unplaced_fruits += 1
        
        return number_of_unplaced_fruits