# 2239.) Find Closest Number to Zero
# Categories: Array

class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        def convertToPositiveNumber(number: int) -> int:
            return int(str(number).replace('-', ''))

        distances = {}
    
        for i in range(len(nums)):
            distance = nums[i] - 0
            
            if distance < 0:
                distance = convertToPositiveNumber(distance)

            distances[nums[i]] = distance
        
        closest_distance = min(list(distances.values()))
        element_with_closest_distance = []
        
        for element, distance in distances.items():
            if closest_distance == distance:
                element_with_closest_distance.append(element)
        
        element_with_closest_distance = sorted(element_with_closest_distance, reverse=True)
        
        return element_with_closest_distance[0]

                