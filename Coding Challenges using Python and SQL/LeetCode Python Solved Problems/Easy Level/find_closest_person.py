# 3516.) Find Closest Person
# Categories: Math

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        person_1_distance_to_person_3 = abs(x - z)
        person_2_distance_to_person_3 = abs(y - z)

        if person_1_distance_to_person_3 < person_2_distance_to_person_3:
            return 1
        

        elif person_2_distance_to_person_3 < person_1_distance_to_person_3:
            return 2
        
        return 0