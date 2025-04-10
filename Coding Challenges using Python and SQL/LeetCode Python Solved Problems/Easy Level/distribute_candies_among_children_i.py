# 2928.) Distribute Candies Among Children I
# Categories: Math, Combinatorics, Enumeration

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        list_of_distributions_of_candies = []

        for i in range(n + 1):
            for j in range(n + 1):
                for k in range(n + 1):
                    if (i > limit) or (j > limit) or (k > limit):
                        continue

                    if sum([i, j, k]) != n:
                        continue
                    
                    list_of_distributions_of_candies.append(tuple([i, j, k]))
        
        return len(set(list_of_distributions_of_candies))

                                