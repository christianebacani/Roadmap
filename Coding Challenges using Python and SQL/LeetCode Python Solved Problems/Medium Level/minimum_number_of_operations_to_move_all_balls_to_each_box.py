# 1769.) Minimum Number of Operations to Move All Balls to Each Box
# Categories: Array, String, Prefix Sum

from typing import List
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        
        for i in range(len(boxes)):
            indices_of_box_with_ball = []

            for j in range(len(boxes)):
                if i != j and boxes[j] == '1':
                    indices_of_box_with_ball.append(j)
            
            total_operations = 0
            
            for j in range(len(indices_of_box_with_ball)):
                total_operations += abs(i - indices_of_box_with_ball[j])
            
            answer.append(total_operations)
        
        return answer