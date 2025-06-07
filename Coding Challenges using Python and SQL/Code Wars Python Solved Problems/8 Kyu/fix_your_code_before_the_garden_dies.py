# Question: Fix your code before the garden dies!
# Categories: 8 Kyu

def rain_amount(mm: int) -> str:
    rain_amount = 40
    
    if mm < 40:
        return "You need to give your plant " + str(rain_amount - mm) + "mm of water"
    
    else:
        return "Your plant has had more than enough water for today!"