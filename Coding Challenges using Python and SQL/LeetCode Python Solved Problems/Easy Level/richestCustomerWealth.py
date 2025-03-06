# 1672.) Richest Customer Wealth
# Categories: Array, Matrix

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0

        for account in accounts:
            account_wealth = sum(account)

            if account_wealth >= max_wealth:
                max_wealth = account_wealth

        return max_wealth
