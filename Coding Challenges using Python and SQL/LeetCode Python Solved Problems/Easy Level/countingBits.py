# 338.) Counting Bits
# Categories: Dynamic Programming, Bit Manipulation

class Solution:
    def countBits(self, n: int) -> list[int]:
        def convert_to_bin(num: int) -> str:
            binary = ''
            
            while num > 0:
                remainder = num % 2
                binary = str(remainder) + binary
                num = num // 2
            
            return binary
        
        answer = []

        for i in range(0, n + 1):
            binary = convert_to_bin(i)
            count = 0

            for j in range(len(binary)):
                if binary[j] == '1':
                    count += 1

            answer.append(count)

        return answer