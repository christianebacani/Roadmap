# 748.) Shortest Completing Word
# Categories: Array, Hash Table, String

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        alphabets = [
            'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p',
            'q', 'r', 's', 't',
            'u', 'v', 'w', 'x',
            'y', 'z'
        ]
        licensePlateChars = []

        for i in range(len(licensePlate)):
            if licensePlate[i].lower() in alphabets:
                licensePlateChars.append(licensePlate[i].lower())
        
        complete_words_and_sizes = {}
    
        for i in range(len(words)):
            word = words[i].lower()
            is_complete_word = True

            for j in range(len(licensePlateChars)):
                if licensePlateChars.count(licensePlateChars[j]) > word.count(licensePlateChars[j]):
                    is_complete_word = False
                    break

            if is_complete_word:
                complete_words_and_sizes[words[i]] = len(word)
    
        minimum_size = min(list(complete_words_and_sizes.values()))

        for word, size in complete_words_and_sizes.items():
            if minimum_size == size:
                return word    