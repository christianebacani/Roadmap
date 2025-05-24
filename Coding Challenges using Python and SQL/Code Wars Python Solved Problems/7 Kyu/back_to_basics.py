# Question: Back to Basics
# Categories: 7 Kyu

def types(x : int | float | str | bool) -> str:
    if x is True or x is False:
        return 'bool'

    elif isinstance(x, int):
        return 'int'
    
    elif isinstance(x, float):
        return 'float'
    
    else:
        return 'str'