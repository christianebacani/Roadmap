# 3190.) Find Minimum Operations to Make All Elements Divisble by Three
# Categories : Array, Math

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        number_of_operations = 0

        for num in nums:
            if num % 3 == 0:
                continue

            num_increment = num + 1
            num_decrement = num - 1

            if num_increment % 3 == 0:
                number_of_operations += 1
        
            elif num_decrement % 3 == 0: 
                number_of_operations += 1
    
        return number_of_operations


