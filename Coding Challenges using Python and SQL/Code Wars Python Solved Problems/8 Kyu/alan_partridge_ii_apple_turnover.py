# Question: Alan Partridge II - Apple Turnover
# Categories: 8 Kyu

def apple(x: int) -> str:
    if not isinstance(x, int):
        x = int(x)
    
    if (x ** 2) > 1000:
        return 'It\'s hotter than the sun!!'
    
    return 'Help yourself to a honeycomb Yorkie for the glovebox.'