# Question: Reversed Words
# Categories: 8 Kyu

def reverse_words(s: str) -> str:
    return ' '.join(s.split()[::-1])