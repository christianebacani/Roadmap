# 3360.) Stone Removal Game
# Categories: Math, Simulation

class Solution:
    def canAliceWin(self, n: int) -> bool:
        for index, i in enumerate(range(10, 0, -1)):
            if i <= n:
                n -= i
                continue
            
            if index % 2 != 0:
                return True
            
            return False