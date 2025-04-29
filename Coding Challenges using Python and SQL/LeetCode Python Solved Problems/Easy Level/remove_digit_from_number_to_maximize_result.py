# 2259.) Remove Digit From Number to Maximize Result
# Categories: String, Greedy, Enumeration

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        frequency_of_digit = number.count(digit)
        numbers_after_removing_digit = []

        for _ in range(frequency_of_digit):
            for i in range(len(number)):
                if number[i] != digit:
                    continue
                
                previous_numbers = number[:i]
                next_numbers = number[i + 1:]

                if int(previous_numbers + next_numbers) not in numbers_after_removing_digit:
                    numbers_after_removing_digit.append(int(previous_numbers + next_numbers))
        
        return str(max(numbers_after_removing_digit))