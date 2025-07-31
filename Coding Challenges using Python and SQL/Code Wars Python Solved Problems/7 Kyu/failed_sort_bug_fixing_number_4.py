# Question: Failed Sort - Bug Fixing #4
# Categories: 7 Kyu

def sort_array(value: str) -> str:
    value = list(value)
    value.sort()
    return ''.join(value)