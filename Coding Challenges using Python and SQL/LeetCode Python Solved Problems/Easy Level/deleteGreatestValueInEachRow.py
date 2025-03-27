# 2500.) Delete Greatest Value in Each Row
# Categories: Array, Sorting, Heap(Priority Queue), Matrix, Simulation

class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        num_of_elements_per_row = len(grid[0])
        maximum_deleted_elements = []
        
        for _ in range(num_of_elements_per_row):    
            deleted_elements = []
            
            for i in range(len(grid)):
                deleted_elements.append(max(grid[i]))
                grid[i].remove(max(grid[i]))

            maximum_deleted_elements.append(max(deleted_elements))

        return sum(maximum_deleted_elements)
        
