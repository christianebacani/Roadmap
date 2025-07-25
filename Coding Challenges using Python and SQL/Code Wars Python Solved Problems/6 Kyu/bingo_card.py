# Question: Bingo Card
# Categories: 6 Kyu

import random

def get_bingo_card() -> list[str]:
    columns_and_numbers = {
        'B': [],
        'I': [],
        'N': [],
        'G': [],
        'O': []
    }

    for column, numbers in columns_and_numbers.items():
        if column != 'N':
            i = 0

            while i < 5:
                if column == 'B':
                    random_number = random.randint(1, 15)
                
                elif column == 'I':
                    random_number = random.randint(16, 30)
                
                elif column == 'G':
                    random_number = random.randint(46, 60)
                
                else:
                    random_number = random.randint(61, 75)

                if random_number not in numbers:
                    numbers.append(random_number)
                    i += 1
        
        else:
            i = 0

            while i < 4:
                random_number = random.randint(31, 45)

                if random_number not in numbers:
                    numbers.append(random_number)
                    i += 1
    
    result = []

    for column, numbers in columns_and_numbers.items():
        for number in numbers:
            result.append(f'{column}{str(number)}')
    
    return result