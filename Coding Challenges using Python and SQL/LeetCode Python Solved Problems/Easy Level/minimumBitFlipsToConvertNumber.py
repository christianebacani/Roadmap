# 2220.) Minimum Bit Flips to Convert Number
# Categories: Bit Manipulation

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def converToBinary(num: int) -> str:
            binary = ''
            while num > 0:
                remainder = num % 2
                binary = f'{remainder}{binary}'
                num = num // 2
        
            return binary

        if start == goal:
            return 0
    
        binary_start = converToBinary(start)
        binary_goal = converToBinary(goal)

        if len(binary_start) < len(binary_goal):
            difference = len(binary_goal) - len(binary_start)
            binary_start = ('0' * difference) + binary_start
    
        elif len(binary_goal) < len(binary_start):
            difference = len(binary_start) - len(binary_goal)
            binary_goal = ('0' * difference) + binary_goal

        minimum_number_of_flips = 0

        for index_start, bit_start in enumerate(binary_start):
            for index_goal, bit_goal in enumerate(binary_goal):
                if (index_start == index_goal) and (bit_start != bit_goal):
                    minimum_number_of_flips += 1

        return minimum_number_of_flips