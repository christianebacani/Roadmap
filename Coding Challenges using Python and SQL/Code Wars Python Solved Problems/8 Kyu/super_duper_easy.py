# Question: Super Duper Easy
# Categories: 8 Kyu

def problem(a: int | str) -> int | str:
    if isinstance(a, str):
        return 'Error'

    return (a * 50) + 6