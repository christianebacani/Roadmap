# 1160.) Find Words That Can Be Formed By Characters
# Categories: Array, Hash Table, String, Counting

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        sum = 0

        for i in range(len(words)):
            good = True

            for j in range(len(words[i])):
                if words[i].count(words[i][j]) > chars.count(words[i][j]):
                    good = False
                    break

            if good:
                sum += len(words[i])

        return sum