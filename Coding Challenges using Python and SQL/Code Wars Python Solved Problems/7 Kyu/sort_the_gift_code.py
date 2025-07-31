# Question: Sort the Gift Code
# Categories: 7 Kyu

def sort_gift_code(code: str) -> str:
    code = list(code)
    code.sort()
    return ''.join(code)