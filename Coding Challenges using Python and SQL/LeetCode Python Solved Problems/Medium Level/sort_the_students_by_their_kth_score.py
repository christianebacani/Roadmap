# 2545.) Sort the Students by Their Kth Score
# Categories: Array, Sorting, Matrix

from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        exam_score_of_k_exam = []

        for i in range(len(score)):
            exam_score_of_k_exam.append(score[i][k])
        
        exam_score_of_k_exam = sorted(exam_score_of_k_exam, reverse=True)
        sorted_students = []

        for i in range(len(exam_score_of_k_exam)):
            for j in range(len(score)):
                if exam_score_of_k_exam[i] == score[j][k]:
                    sorted_students.append(score[j])
        
        return sorted_students