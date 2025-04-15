# 2264.) Largest 3-Same-Digvit Number in String
# Categories: String

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_integers = []

        for i in range(2, len(num)):
            if num[i - 2] == num[i - 1] == num[i]:
                good_integers.append(num[i - 2] + num[i - 1] + num[i])
        
        good_integers = sorted(good_integers, reverse=True)
        
        if good_integers != []:
            return good_integers[0]
    
        return ''