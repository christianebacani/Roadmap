# Question: Basic Mathematical Operations
# Categories: 8 Kyu

import math

def basic_op(operator: str, value1: int, value2: int) -> int:
    operations = {
        '+': value1 + value2,
        '-': value1 - value2,
        '*': value1 * value2,
        '/': value1 / value2
    }

    return operations[operator]

if __name__ == '__main__':
    print(basic_op('/', 5, 49))