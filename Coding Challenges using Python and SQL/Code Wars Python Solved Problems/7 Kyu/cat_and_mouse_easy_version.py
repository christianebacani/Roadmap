# Question: Cat and Mouse - Easy Version
# Categories: 7 Kyu

def cat_mouse(x: str) -> str:
    if x.count('.') <= 3:
        return 'Caught!'
    
    return 'Escaped!'