# 3280.) Convert Date to Binary
# Categories : Math, String

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        def convertToBinary(num: int) -> str:
            binary = ''
    
            while num > 0:
                remainder = num % 2
                binary = f'{remainder}{binary}'
                num = int(num / 2)
    
            return binary

        year = convertToBinary(int(date[:4]))
        month = convertToBinary(int(date[5:7]))
        day = convertToBinary(int(date[-2:]))

        return f'{year}-{month}-{day}'