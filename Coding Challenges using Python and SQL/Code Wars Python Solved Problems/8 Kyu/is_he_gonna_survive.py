# Question: Is he gonna survive?
# Categories: 8 Kyu

def hero(bullets, dragons) -> bool:
    if bullets >= dragons * 2:
        return True
    
    return False