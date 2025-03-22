# 2119.) A Number After a Double Reversal
# Categories: Math

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        integer_number = num
        string_number = str(num)

        for _ in range(2):
            if (string_number[-1] == '0') and (string_number != '0'):
                string_number = string_number[::-1]
                
                for string_num in string_number:
                    if string_num == '0':
                        string_number = string_number[1:]

                    else:
                        break

            else:
                string_number = string_number[::-1]
        
        if int(string_number) == integer_number:
            return True
        
        return False
