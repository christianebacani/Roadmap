# 1394.) Find Lucky Integer in an Array
# Categories: Array, Hash Table, Counting

class Solution:
    def findLucky(self, arr: list[int]) -> int:
        frequencies = {}

        for i in range(len(arr)):
            frequencies[arr[i]] = arr.count(arr[i])
        
        lucky_integers = []

        for element, frequency in frequencies.items():
            if element == frequency:
                lucky_integers.append(element)
            
        lucky_integers = sorted(lucky_integers, reverse=True)

        if lucky_integers != []:
            return lucky_integers[0]
    
        return -1