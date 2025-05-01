# 441.) Arranging Coins
# Categories: Math, Binary Search

class Solution:
    def arrangeCoins(self, n: int) -> int:
        complete_rows = 0
        number_of_coins = 0

        while n > 0:
            number_of_coins += 1
            n = n - number_of_coins

            if n >= 0:
                complete_rows += 1

        return complete_rows