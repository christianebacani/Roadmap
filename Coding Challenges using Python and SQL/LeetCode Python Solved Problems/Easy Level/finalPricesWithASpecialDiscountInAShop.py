# 1475.) Final Prices With a Special Discount in a Shop
# Categories: Array, Stack, Monotonic Stack

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        answer = []
    
        for i in range(len(prices)):
            discounted = False

            for j in range(len(prices)):
                if (j > i) and (prices[j] <= prices[i]):
                    answer.append(prices[i] - prices[j])
                    discounted = True
                    break
        
            if not discounted:
                answer.append(prices[i])

        return answer
            
