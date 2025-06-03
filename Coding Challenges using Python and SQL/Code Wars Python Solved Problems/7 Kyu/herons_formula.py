# Question: Heron's formula
# Categories: 7 Kyu
import math

def heron(a: int, b: int, c: int) -> float | int:
    s = (a + b + c) / 2
    answer = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return answer