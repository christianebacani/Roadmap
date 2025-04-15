# 1779.) Find Nearest Point That Has the Same X or Y Coordinate
# Categories: Array

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        indices_and_manhattan_distance = {}
        
        for i in range(len(points)):
            if (points[i][0] == x) or (points[i][1] == y):
                indices_and_manhattan_distance[i] = abs(x - points[i][0]) + abs(y - points[i][1])
        
        smallest_manhattan_distance = min(list(indices_and_manhattan_distance.values()), default=0)

        for index, manhattan_distance in indices_and_manhattan_distance.items():
            if smallest_manhattan_distance == manhattan_distance:
                return index
        
        return -1