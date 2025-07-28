# Question: Compare within margin
# Categories: 8 Kyu

def close_compare(a: int, b: int, margin=0):
    if margin >= abs(a - b):
        return 0
    
    elif a < b:
        return -1
    
    else:
        return 1