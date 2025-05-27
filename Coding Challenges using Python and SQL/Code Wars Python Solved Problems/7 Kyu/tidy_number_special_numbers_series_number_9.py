# Question: Tidy Number (Special Numbers Series #9)
# Categories: 7 Kyu

def tidyNumber(n: int) -> bool:
    digits = [num for num in str(n)]

    return digits == sorted(digits)