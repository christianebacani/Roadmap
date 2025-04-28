# 2806.) Account Balance After Rounded Purchase
# Categories: Math

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        multiple_of_10s = [
            0, 10, 20, 30, 40, 50,
            60, 70, 80, 90, 100
        ]
        
        distances_to_multiple_10s = {}

        for i in range(len(multiple_of_10s)):
            distances_to_multiple_10s[multiple_of_10s[i]] = abs(multiple_of_10s[i] - purchaseAmount)
        
        nearest_distance_to_multiple_of_10s = min(list(distances_to_multiple_10s.values()))
        multiple_of_10s_with_nearest_distance = []
        
        for multiple_of_10s, distance in distances_to_multiple_10s.items():
            if nearest_distance_to_multiple_of_10s == distance:
                multiple_of_10s_with_nearest_distance.append(multiple_of_10s)
        
        return 100 - max(multiple_of_10s_with_nearest_distance)