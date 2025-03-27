# 1725.) Number Of Rectangles That Can Form The Largest Square
# Categories: Array

class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        rectangle_side_lengths = []
        
        for i in range(len(rectangles)):
            rectangle_side_lengths.append(min(rectangles[i][0], rectangles[i][1]))
    
        maximum_side_length = max(rectangle_side_lengths, default=0)
        count_of_good_rectangles = rectangle_side_lengths.count(maximum_side_length)
        
        return count_of_good_rectangles

