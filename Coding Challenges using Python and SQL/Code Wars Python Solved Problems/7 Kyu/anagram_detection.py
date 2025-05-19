# Question: Anagram Detection
# Categories: 7 Kyu

def is_anagram(test: str, original: str) -> bool:
    if sorted(list(test.lower())) == sorted(list(original.lower())):
        return True
    
    return False