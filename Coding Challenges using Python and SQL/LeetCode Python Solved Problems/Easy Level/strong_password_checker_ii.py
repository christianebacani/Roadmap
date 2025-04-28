# 2299.) Strong Password Checker II
# Categories: String

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        def checkIfPassContainsAtleast8LengthChar(password: str) -> bool:
            if len(password) < 8:
                return False
        
            return True
    
        def checkIfPassContainsAtleastOneLowerChar(password: str) -> bool:
            for i in range(len(password)):
                if password[i].islower():
                    return True
        
            return False
    
        def checkIfPassContainsAtleastOneUpperChar(password: str) -> bool:
            for i in range(len(password)):
                if password[i].isupper():
                    return True
        
            return False
    
        def checkIfPassContainsAtleastOneDigit(password: str) -> bool:
            for i in range(len(password)):
                if password[i].isdigit():
                    return True
        
            return False
    
        def checkIfPassContainsAtleastOneSpecChar(password: str) -> bool:
            special_characters = '!@#$%^&*()-+'

            for i in range(len(password)):
                if password[i] in special_characters:
                    return True
        
            return False
    
        def checkIfPassNotContainsAdjaChars(password: str) -> bool:
            for i in range(1, len(password)):
                if password[i - 1] == password[i]:
                    return False
        
            return True
    
        if checkIfPassContainsAtleast8LengthChar(password) and checkIfPassContainsAtleastOneLowerChar(password) and checkIfPassContainsAtleastOneUpperChar(password) and checkIfPassContainsAtleastOneDigit(password) and checkIfPassContainsAtleastOneSpecChar(password) and checkIfPassNotContainsAdjaChars(password):
            return True
    
        return False