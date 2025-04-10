# 506.) Relative Ranks
# Categories: Array, Sorting, Heap (Priority Queue)

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_scores = sorted(score, reverse=True)
        medals = {}

        for i in range(len(sorted_scores)):
            if i == 0:
                medals[sorted_scores[i]] = 'Gold Medal'
            
            elif i == 1:
                medals[sorted_scores[i]] = 'Silver Medal'
            
            elif i == 2:
                medals[sorted_scores[i]] = 'Bronze Medal'
            
            else:
                medals[sorted_scores[i]] = str(i + 1)
        
        answer = []

        for i in range(len(score)):
            answer.append(medals[score[i]])
        
        return answer