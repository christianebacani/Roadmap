# Question: Find the calculation type
# Categories: 7 Kyu

def calc_type(a: int, b: int, result: int) -> str:
    operation_and_results = {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b
    }

    for operation, operation_result in operation_and_results.items():
        if result == operation_result:
            return operation