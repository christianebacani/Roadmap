# 3417.) Zigzag Grid Traversal With Skip
# Categories: Array, Matrix, Simulation

class Solution:
    def zigzagTraversal(self, grid: list[list[int]]) -> list[int]:
        answer = []

        if len(grid[0]) % 2 == 0:
            for i in range(len(grid)):
                if i % 2 == 0:
                    for j in range(len(grid[i])):
                        if j % 2 == 0:
                            answer.append(grid[i][j])
                
                else:
                    for j in range(len(grid[i][::-1])):
                        if j % 2 == 0:
                            answer.append(grid[i][::-1][j])
        
        else:
            for i in range(len(grid)):
                if i % 2 == 0:
                    for j in range(len(grid[i])):
                        if j % 2 == 0:
                            answer.append(grid[i][j])

                else:
                    for j in range(len(grid[i][::-1])):
                        if j % 2 != 0:
                            answer.append(grid[i][::-1][j])

        return answer