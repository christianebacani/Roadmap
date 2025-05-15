# Question: Write a function to check if a given number is a Pronic number or not
# Categories: Medium

def is_pronic(n : int) -> True:
    for i in range(n + 1):
        if i * (i + 1) == n:
            return True
    
    return False