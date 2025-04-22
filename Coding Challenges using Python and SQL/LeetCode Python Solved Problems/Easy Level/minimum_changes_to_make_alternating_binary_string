# 1758.) Minimum Changes to Make Alternating Binary String
# Categories: String

class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1:
            return 0

        first_alternate_s = ('0' * (len(s) % 2)) + ('10' * (len(s) // 2))
        second_alternate_s = ('1' * (len(s) % 2)) + ('01' * (len(s) // 2))

        number_of_operations_for_first_alternate_s = 0
        number_of_operations_for_second_alternate_s = 0
        
        for i in range(len(first_alternate_s)):
            if first_alternate_s[i] != s[i]:
                number_of_operations_for_first_alternate_s += 1
        
        for i in range(len(second_alternate_s)):
            if second_alternate_s[i] != s[i]:
                number_of_operations_for_second_alternate_s += 1
        
        if number_of_operations_for_first_alternate_s <= number_of_operations_for_second_alternate_s:
            return number_of_operations_for_first_alternate_s
        
        return number_of_operations_for_second_alternate_s