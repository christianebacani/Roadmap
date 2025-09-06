# Question: Ensure question
# Categories: 8 Kyu

def ensure_question(s: str) -> str:
    if s == '':
        return '?'

    if s[-1] == '?':
        return s

    return s + '?'