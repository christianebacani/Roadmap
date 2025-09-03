# Question: Is your period late?
# Categories: 8 Kyu

def period_is_late(last,today,cycle_length) -> bool:
    difference = today - last
    difference = difference.days
    
    return difference > cycle_length