# 1556.) Thousand Separator
# Categories: String

class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = list(str(n)[::-1])
        dot_separated_n = []

        for index, num in enumerate(n):
            index += 1

            dot_separated_n.append(num)
            
            if index % 3 == 0:
                dot_separated_n.append('.')
        
        dot_separated_n = ''.join(dot_separated_n)[::-1]

        if dot_separated_n[0] == '.':
            dot_separated_n = dot_separated_n[1:]

        return dot_separated_n