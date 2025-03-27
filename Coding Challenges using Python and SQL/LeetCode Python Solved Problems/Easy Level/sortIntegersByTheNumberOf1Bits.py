# 1356.) Sort Integers by The Number of 1 Bits
# Categories: Array, Bit Manipulation, Sorting, Counting

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        bits_count = {}
        result = []

        for i in range(len(arr)):
            binary = bin(arr[i])[2:]
            bits_count[arr[i]] = binary.count('1')

        sorted_bits_count = sorted(list(set(bits_count.values())))
        
        for bits_count in sorted_bits_count:
            numbers = []
            
            for i in range(len(arr)):
                count = bin(arr[i])[2:].count('1')

                if bits_count == count:
                    numbers.append(arr[i])

            result.extend(sorted(numbers))
        
        return result    