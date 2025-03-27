# 1704.) Determine if String Halves Are Alike
# Categories: String, Counting

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        index_delimiter = len(s) // 2
        a = s[ : index_delimiter].lower()
        b = s[index_delimiter : ].lower()

        vowels = ['a', 'e', 'i', 'o', 'u']
        
        number_of_vowels_from_a = 0
        number_of_vowels_from_b = 0
        
        for i in range(len(a)):
            if a[i] in vowels:
                number_of_vowels_from_a += 1
        
        for i in range(len(b)):
            if b[i] in vowels:
                number_of_vowels_from_b += 1
        
        if number_of_vowels_from_a == number_of_vowels_from_b:
            return True
        
        return False
    