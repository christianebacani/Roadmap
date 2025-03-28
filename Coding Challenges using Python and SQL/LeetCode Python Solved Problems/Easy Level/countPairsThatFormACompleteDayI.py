# 3184.) Count Pairs That Form a Complete Day I
# Categories: Array, Hash Table, Counting

class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        pairs = []
        
        for i in range(len(hours)):
            for j in range(len(hours)):
                if (i < j) and ((hours[i] + hours[j]) % 24 == 0):
                    pairs.append(tuple([hours[i], hours[j]]))
        
        return len(pairs)
    