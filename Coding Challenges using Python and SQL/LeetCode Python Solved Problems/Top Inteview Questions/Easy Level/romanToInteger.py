# 13.) Roman to Integer
# Category : Hash Table, Math, String 

class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumeralsDict = {'I' : 1, 'IV' : 4, 'V' : 5, 'IX' : 9,
                             'X' : 10, 'XL' : 40, 'L' : 50, 'XC' : 90, 
                             'C' : 100, 'CD' : 400, 'D' : 500, 'CM' : 900, 'M' : 1000}
    
        specialRomanNumerals = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        num = 0
    
        for romanNumeral in specialRomanNumerals:
            if romanNumeral in s:
                num += romanNumeralsDict[romanNumeral]
                s = s.replace(romanNumeral, '')

        for char in s:
            num += romanNumeralsDict[char]
    
        return num

