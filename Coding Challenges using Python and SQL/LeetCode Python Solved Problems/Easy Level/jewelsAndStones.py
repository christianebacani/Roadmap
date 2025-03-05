# 771.) Jewels and Stones
# Categories : Hash Table, String

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        list_of_jewels = []
        number_of_jewels = 0

        for jewel in jewels:
            if jewel not in list_of_jewels:
                list_of_jewels.append(jewel)
    
        for stone in stones:
            if stone in list_of_jewels:
                number_of_jewels += 1
    
        return number_of_jewels
