# 1496.) Path Crossing
# Categories: Hash Table, String

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        origin = [0, 0]
        previously_visited_points = [(0, 0)]

        for i in range(len(path)):
            if path[i] == 'N':
                origin[1] += 1
            
            elif path[i] == 'S':
                origin[1] -= 1
            
            elif path[i] == 'E':
                origin[0] += 1
            
            else:
                origin[0] -= 1

            previously_visited_points.append(tuple(origin))
    
        if len(set(previously_visited_points)) != len(previously_visited_points):
            return True
        
        return False