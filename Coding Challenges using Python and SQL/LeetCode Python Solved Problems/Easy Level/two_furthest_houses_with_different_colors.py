# 2078.) Two Furthest Houses With Different Colors
# Categories: Array, Greedy

class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        furthest_distances = []

        for i in range(len(colors)):
            distances = []

            for j in range(len(colors)):
                if i != j and colors[i] != colors[j]:
                    distances.append(abs(i - j))
            
            furthest_distances.append(max(distances))
        
        return max(furthest_distances)