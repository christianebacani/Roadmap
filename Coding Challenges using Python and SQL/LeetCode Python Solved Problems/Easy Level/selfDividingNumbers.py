# 728.) Self Dividing Numbers
# Categories: Math

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        self_dividing_number_list = []

        for i in range(left, right + 1):
            number = str(i)
            
            if '0' in number:
                continue

            self_dividing_number = True

            for j in range(len(number)):
                if int(number) % int(number[j]) != 0:
                    self_dividing_number = False
            
            if self_dividing_number:
                self_dividing_number_list.append(int(number))

        return self_dividing_number_list
        
            

            