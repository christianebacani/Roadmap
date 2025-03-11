# 3285.) Find Indices of Stable Mountains
# Categories: Array

class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        stable_mountains_indices = []

        for i in range(len(height)):
            if i - 1 < 0:
                continue
        
            if height[i - 1] > threshold:
                stable_mountains_indices.append(i)
    
        return stable_mountains_indices
