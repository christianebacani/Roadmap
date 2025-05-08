# 692.) Top K Frequent Words
# Categories: Array, Hash Table, String, Trie, Sorting, Heap (Priority Queue), Bucket Sort, Counting

from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_and_frequencies = {}

        for i in range(len(words)):
            words_and_frequencies[words[i]] = words.count(words[i])
    
        sorted_frequencies = sorted(list(words_and_frequencies.values()), reverse=True)
        answer = []

        for i in range(len(sorted_frequencies)):
            words_with_equal_frequencies = []
            
            for word, frequency in words_and_frequencies.items():
                if sorted_frequencies[i] == frequency:
                    words_with_equal_frequencies.append(word)
            
            words_with_equal_frequencies = sorted(words_with_equal_frequencies)

            for j in range(len(words_with_equal_frequencies)):
                if words_with_equal_frequencies[j] in answer:
                    continue

                answer.append(words_with_equal_frequencies[j])
        
        answer = answer[:k]

        return answer