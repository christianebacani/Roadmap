# 682.) Baseball Game
# Categories: Array, Stack, Simulation

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        
        for i in range(len(operations)):
            try:
                if int(operations[i]):
                    record.append(int(operations[i]))

            except ValueError:
                if operations[i] == '+':
                    record.append(sum(record[-2:]))
                    
                elif operations[i] == 'D':
                    record.append(record[-1] * 2)
            
                else:
                    record.pop(-1)
        
        return sum(record)
