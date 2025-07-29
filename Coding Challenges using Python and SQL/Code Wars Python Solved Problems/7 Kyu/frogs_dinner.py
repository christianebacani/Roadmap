# Question: Frog's Dinner
# Categories: 7 Kyu

import math

def frog_contest(flies: str) -> str:
    chris_total_flies = 0
    tom_total_flies = 0
    cat_total_flies = 0

    for i in range(1, flies + 1):
        chris_total_flies += i
    
    for i in range(1, math.floor(chris_total_flies / 2) + 1):
        tom_total_flies += i
    
    for i in range(1, (chris_total_flies + tom_total_flies) + 1):
        cat_total_flies += i
    
    return f'Chris ate {chris_total_flies} flies, Tom ate {tom_total_flies} flies and Cat ate {cat_total_flies} flies'