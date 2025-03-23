# 2103.) Rings and Rods
# Categories: Hash Table, String

class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {
            0: [], 1: [], 2: [],
            3: [], 4: [], 5: [],
            6: [], 7: [], 8: [],
            9: []
        }
        
        for i in range(0, len(rings), 2):
            rod_position = int(rings[i + 1])
            rods[rod_position].append(rings[i])
        
        count = 0

        for rod_position, ring_colors in rods.items():
            if 'R' in ring_colors and 'G' in ring_colors and 'B' in ring_colors:
                count += 1
        
        return count


        