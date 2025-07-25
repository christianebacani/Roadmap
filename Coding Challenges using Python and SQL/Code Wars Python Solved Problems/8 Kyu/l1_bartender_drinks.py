# Question: L1:Bartender, drinks!
# Categories: 8 Kyu

def get_drink_by_profession(param: str) -> str:
    profession_drinks = {
        'Jabroni': 'Patron Tequila',
        'School Counselor': 'Anything with Alcohol',
        'Programmer': 'Hipster Craft Beer',
        'Bike Gang Member': 'Moonshine',
        'Politician': 'Your tax dollars',
        'Rapper': 'Cristal'
    }
    param = param.split()

    for i in range(len(param)):
        param[i] = param[i].capitalize()
    
    param = ' '.join(param)

    if param not in profession_drinks:
        return 'Beer'
    
    return profession_drinks[param]