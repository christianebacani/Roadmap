# Question: Make a function that does arithmetic!
# Categories: 7 Kyu

def arithmetic(a: int, b: int, operator: str) -> int | float:
    operations = {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b
    }

    return operations[operator]