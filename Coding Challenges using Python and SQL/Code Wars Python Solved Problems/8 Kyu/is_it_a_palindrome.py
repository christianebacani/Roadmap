# Question: Is it a palindrome?
# Categories: 8 Kyu

def is_palindrome(s: str) -> bool:
    return s.lower() == s[::-1].lower()