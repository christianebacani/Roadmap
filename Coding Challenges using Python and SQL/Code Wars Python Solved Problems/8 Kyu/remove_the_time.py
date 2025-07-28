# Question: Remove the time
# Categories: 8 Kyu

def shorten_to_date(long_date: str) -> str:
    result = long_date.split(',')[0]
    return result