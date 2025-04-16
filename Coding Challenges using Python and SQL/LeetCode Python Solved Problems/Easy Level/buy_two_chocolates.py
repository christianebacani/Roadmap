# 2706.) Buy Two Chocolates
# Categories: Array, Greedy, Sorting

class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices = sorted(prices)
        
        if (prices[0] + prices[1]) <= money:
            return money - (prices[0] + prices[1])

        return money