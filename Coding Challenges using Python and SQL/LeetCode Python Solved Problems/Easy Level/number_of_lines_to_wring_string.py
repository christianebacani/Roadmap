# 806.) Number of Lines To Write String
# Categories: Array, String

from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        alphabets = [
            'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
            'u', 'v', 'w', 'x',
            'y', 'z'
        ]
        width_of_every_chars = []

        for i in range(len(s)):
            width_of_every_chars.append(widths[alphabets.index(s[i])])

        width_per_lines = []

        while len(width_of_every_chars) != 0:
            index_delimiter = 0
            line = []

            for i in range(len(width_of_every_chars)):
                if line == []:
                    line.append(width_of_every_chars[i])
                    index_delimiter = i + 1
                    continue

                if width_of_every_chars[i] + sum(line) > 100:
                    break
                
                else:
                    line.append(width_of_every_chars[i])
                    index_delimiter = i + 1

            width_per_lines.append(line)
            width_of_every_chars = width_of_every_chars[index_delimiter:]

        ans = [len(width_per_lines), sum(width_per_lines[-1])]

        return ans