# 2144.) Minimum Cost of Buying Candies With Discount
# Categories: Array, Greedy, Sorting

class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        minimum_cost = 0

        while len(cost) != 0:
            cost = sorted(cost, reverse=True)
            
            try:
                minimum_cost += cost[0]
            
            except IndexError:
                pass

            try:
                minimum_cost += cost[1]
            
            except IndexError:
                pass
            
            cost = cost[3:]

        return minimum_cost