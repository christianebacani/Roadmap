# 657.) Robot Return to Origin
# Categories: String, Simulation

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position = [0, 0]
        
        for i in range(len(moves)):
            if moves[i] == 'U':
                position[1] += 1
            
            elif moves[i] == 'D':
                position[1] -= 1
            
            elif moves[i] == 'L':
                position[0] -= 1
            
            else:
                position[0] += 1
        
        if position == [0, 0]:
            return True
    
        return False
    