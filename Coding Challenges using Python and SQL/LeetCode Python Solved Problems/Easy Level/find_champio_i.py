# 2923.) Find Champion I
# Categories: Array, Matrix

class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        points_per_team = {}

        for i in range(len(grid)):
            total_points = []

            for j in range(len(grid[i])):
                if i != j:
                    total_points.append(grid[i][j])
            
            points_per_team[i] = total_points.count(1)
        
        maximum_points = max(list(points_per_team.values()))

        for team, points in points_per_team.items():
            if maximum_points == points:
                return team
            