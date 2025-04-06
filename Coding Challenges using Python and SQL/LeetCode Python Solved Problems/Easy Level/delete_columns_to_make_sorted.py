# 944.) Delete Columns to Make Sorted
# Categories: Array, String

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        def getAlphabeticalOrder(char: str) -> int:
            alphabets = [
                'a', 'b', 'c', 'd',
                'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p',
                'q', 'r', 's', 't',
                'u', 'v', 'w', 'x',
                'y', 'z'
            ]
            
            for index, letter in enumerate(alphabets):
                if char == letter:
                    return index + 1
        
        number_of_columns = len(strs[0])
        number_of_columns_to_delete = 0

        for column in range(number_of_columns):
            alphabetical_orders = []
            
            for element in strs:
                alphabetical_orders.append(getAlphabeticalOrder(element[column]))
            
            for i in range(1, len(alphabetical_orders)):
                if alphabetical_orders[i - 1] > alphabetical_orders[i]:
                    number_of_columns_to_delete += 1
                    break

        return number_of_columns_to_delete
