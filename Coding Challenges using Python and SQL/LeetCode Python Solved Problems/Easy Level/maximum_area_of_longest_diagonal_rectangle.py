# 3000.) Maximum Area of Longest Diagonal Rectangle
# Categories: Array

from typing import List
import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        length_width_and_diagonal_lengths = {}

        for i in range(len(dimensions)):
            length = dimensions[i][0]
            width = dimensions[i][1]
            
            length_width_and_diagonal_lengths[tuple([length, width])] = round(math.sqrt((length * length) + (width * width)), 3)
        
        maximum_diagonal_length = max(list(length_width_and_diagonal_lengths.values()))
        dimensions_with_highest_diagonal_length = []

        for length_width, diagonal_length in length_width_and_diagonal_lengths.items():
            if maximum_diagonal_length == diagonal_length:
                dimensions_with_highest_diagonal_length.append(list(length_width))
        
        if len(dimensions_with_highest_diagonal_length) == 1:
            return dimensions_with_highest_diagonal_length[0][0] * dimensions_with_highest_diagonal_length[0][1]
        
        maximum_area_of_the_rectangle = 0

        for i in range(len(dimensions_with_highest_diagonal_length)):
            length = dimensions_with_highest_diagonal_length[i][0]
            width = dimensions_with_highest_diagonal_length[i][1]

            if length * width > maximum_area_of_the_rectangle:
                maximum_area_of_the_rectangle = length * width
        
        return maximum_area_of_the_rectangle