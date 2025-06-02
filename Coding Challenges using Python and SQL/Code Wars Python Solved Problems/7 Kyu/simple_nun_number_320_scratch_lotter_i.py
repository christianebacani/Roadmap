# Question: Simple Fun #320: Scratch lottery I
# Categories: 7 Kyu

def scratch(lottery: list[str]) -> int:
    total_bonuses = 0

    for i in range(len(lottery)):
        animals = []
        bonus = ''

        for j in range(len(lottery[i].split())):
            if lottery[i].split()[j].isalpha():
                animals.append(lottery[i].split()[j])
        
            else:
                bonus += lottery[i].split()[j]
        
        if len(set(animals)) == 1:
            total_bonuses += int(bonus)
    
    return total_bonuses