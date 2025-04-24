# 2269.) Find the K-Beauty of a Number
# Categories: Math, String, Sliding Window

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        number_of_substrings = 0

        for i in range(len(num)):
            substring = num[i : i + k]

            if set(substring) == {'0'}:
                continue
            
            if len(substring) != k:
                continue

            if int(num) % int(substring) == 0:
                number_of_substrings += 1
        
        return number_of_substrings