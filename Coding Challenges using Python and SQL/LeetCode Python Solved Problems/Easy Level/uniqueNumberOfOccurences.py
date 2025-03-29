# 1207.) Unique Number of Occurences
# Categories: Array, Hash Table

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        frequencies = {}
        
        for i in range(len(arr)):
            frequency = 0
            
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    frequency += 1

            frequencies[arr[i]] = frequency

        number_of_frequencies = list(frequencies.values())
        
        for i in range(len(number_of_frequencies)):
            count = 0
            
            for j in range(len(number_of_frequencies)):
                if number_of_frequencies[i] == number_of_frequencies[j]:
                    count += 1
            
            if count > 1:
                return False
        
        return True
    
        