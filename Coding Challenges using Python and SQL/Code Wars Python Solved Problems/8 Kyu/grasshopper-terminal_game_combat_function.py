# Question: Grasshopper - Terminal game combat function
# Categories: 8 Kyu

def combat(health: int, damage: int) -> int:
    if health >= damage:
        return health - damage
    
    return 0