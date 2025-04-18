# 3206.) Alternating Groups I
# Categories: Array, Sliding Window

class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        alternate_groups = 0

        for i in range(len(colors)):
            if i + 1 > len(colors) - 1:
                if (colors[i] != colors[i - 1]) and (colors[i] != colors[(i + 1) - len(colors)]):
                    alternate_groups += 1
                
                continue
            
            elif (colors[i] != colors[i - 1] and colors[i] != colors[i + 1]):
                alternate_groups += 1
    
        return alternate_groups