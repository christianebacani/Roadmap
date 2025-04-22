# 2094.) Finding 3-Digit Even Numbers
# Categories: Array, Hash Table, Sorting, Enumeration

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        str_digits = [str(num) for num in digits]
        three_digit_even_numbers = []

        for i in range(100, 1000):
            three_digits = str(i)
            three_digits_present_to_str_digits = True

            for j in range(len(three_digits)):
                if three_digits.count(three_digits[j]) > str_digits.count(three_digits[j]):
                    three_digits_present_to_str_digits = False
                    break

            if not three_digits_present_to_str_digits:
                continue

            if int(three_digits) % 2 == 0:
                three_digit_even_numbers.append(int(three_digits))

        three_digit_even_numbers.sort()
        return three_digit_even_numbers