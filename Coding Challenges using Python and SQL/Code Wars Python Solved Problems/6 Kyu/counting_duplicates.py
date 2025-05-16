# Question: Counting Duplicates
# Categories: 6 Kyu

def duplicate_count(text: str) -> int:
    text = text.lower()
    word_and_frequencies = {}

    for i in range(len(text)):
        word_and_frequencies[text[i]] = text.count(text[i])
    
    count_of_duplicates = 0
    frequencies = list(word_and_frequencies.values())

    for i in range(len(frequencies)):
        if frequencies[i] > 1:
            count_of_duplicates += 1
    
    return count_of_duplicates