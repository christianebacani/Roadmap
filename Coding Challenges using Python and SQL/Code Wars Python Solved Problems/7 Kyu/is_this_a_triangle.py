# Question: Is this a triangle?
# Categories: 7 Kyu

def is_triangle(a: int, b: int, c: int) -> True:
    if (a + b <= c) or (b + c <= a) or (a + c <= b):
        return False
    
    return True