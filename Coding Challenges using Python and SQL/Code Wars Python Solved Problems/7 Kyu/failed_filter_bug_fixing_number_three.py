# Question: Failed Filter - Bug Fixing #3
# Categories: 7 Kyu

def filter_numbers(string: str) -> str:
    return "".join(x for x in string if not x.isdigit())