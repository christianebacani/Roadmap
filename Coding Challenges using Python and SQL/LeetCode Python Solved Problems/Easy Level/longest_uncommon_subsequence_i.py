# 521.) Longest Uncommon Subsequence I
# Categories: String

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        distinct_uncommon_subsequence = []

        for i in range(1, len(a) + 1):
            for j in range(len(a)):
                subsequent_a = a[j : j + i]
                
                if subsequent_a in b:
                    continue

                if subsequent_a not in distinct_uncommon_subsequence:
                    distinct_uncommon_subsequence.append(subsequent_a)
        
        for i in range(1, len(b) + 1):
            for j in range(len(b)):
                subsequent_b = b[j : i + i]

                if subsequent_b in a:
                    continue

                if subsequent_b not in distinct_uncommon_subsequence:
                    distinct_uncommon_subsequence.append(subsequent_b)

        maximum_length = -1

        for i in range(len(distinct_uncommon_subsequence)):
            if len(distinct_uncommon_subsequence[i]) > maximum_length:
                maximum_length = len(distinct_uncommon_subsequence[i])

        return maximum_length