# Question: For the sake of argument
# Categories: 7 Kyu

def numbers(*args) -> bool:
    for element in args:
        if isinstance(element, (bool, str)):
            return False
        
        if element is None:
            return False
    
    return True