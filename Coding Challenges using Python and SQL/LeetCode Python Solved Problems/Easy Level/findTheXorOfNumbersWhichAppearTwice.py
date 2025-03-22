# 3158.) Find the XOR of Numbers Which Appear Twice
# Categories: Array, Hash Table, Bit Manipulation

class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        element_and_number_of_apperance = {}
        bitwise_xor = 0
    
        for i in range(len(nums)):
            count = 0

            for j in range(len(nums)):
                if (nums[i] == nums[j]):
                    count += 1

            element_and_number_of_apperance[nums[i]] = count

        for element, number_of_apperance in element_and_number_of_apperance.items():
            if number_of_apperance == 2:
                bitwise_xor ^= element

        return bitwise_xor            
            

            