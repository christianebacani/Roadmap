# 2942.) Find Words Containing Character
# Categories : Array, String

class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        ans = []

        for index, word in enumerate(words):
            word_lst = []

            for char in word:
                word_lst.append(char)

            if x in word_lst:
                ans.append(index)

        return ans
