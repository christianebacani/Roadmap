# Question: Swith it Up!
# Categories: 8 Kyu

def switch_it_up(number: int) -> str:
    number_to_word = {
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten'
    }

    return number_to_word[number]