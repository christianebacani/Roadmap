# 3079.) Find the Sum of Encrypted Integers
# Categories: Array, Math

class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        def encrypt(number: int) -> int:
            number = list(str(number))
            max = 0

            for i in range(len(number)):
                if int(number[i]) > max:
                    max = int(number[i])
            
            for i in range(len(number)):
                number[i] = str(max)
        
            return int(''.join(number))

        sum = 0
        
        for i in range(len(nums)):
            sum += encrypt(nums[i])

        return sum
            
            