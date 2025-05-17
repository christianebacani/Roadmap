# Question: The Feast of Many Beasts
# Categories: 8 Kyu

def feast(beast: str, dish: str) -> bool:
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    
    return False