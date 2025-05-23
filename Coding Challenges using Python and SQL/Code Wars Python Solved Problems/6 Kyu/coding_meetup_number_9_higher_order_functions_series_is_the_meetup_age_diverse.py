# Question: Coding Meetup #9 - Higher-Order Functions Series - Is the meetup age-diverse?
# Categories: 6 Kyu

def is_age_diverse(lst: list[dict[str, str]]): 
    age_and_age_range = {
        'teens': range(10, 20),
        'twenties': range(20, 30),
        'thirties': range(30, 40),
        'forties': range(40, 50),
        'fifties': range(50, 60),
        'sixties': range(60, 70),
        'seventies': range(70, 80),
        'eighties': range(80, 90),
        'nineties': range(90, 100),
        'centenaries': range(100, 200)
    }

    for _, age_range in age_and_age_range.items():
        count = 0

        for i in range(len(lst)):
            if lst[i]['age'] in age_range:
                count += 1
        
        if count == 0:
            return False
    
    return True