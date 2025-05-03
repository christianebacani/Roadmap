# 2423.) Remove Letter To Equalize Frequency
# Categories: Hash Table, String, Counting

class Solution:
    def equalFrequency(self, word: str) -> bool:
        list_of_words_after_removing_one_letter = []

        for i in range(len(word)):
            for j in range(len(word)):
                if i != j:
                    continue
                
                previous_characters = word[:j]
                next_characters = word[j + 1:]

                list_of_words_after_removing_one_letter.append(previous_characters + next_characters)
        
        for i in range(len(list_of_words_after_removing_one_letter)):
            word_after_removing_one_letter = list_of_words_after_removing_one_letter[i]
            frequencies = []

            for j in range(len(word_after_removing_one_letter)):
                frequencies.append(word_after_removing_one_letter.count(word_after_removing_one_letter[j]))
            
            if len(set(frequencies)) == 1:
                return True
        
        return False