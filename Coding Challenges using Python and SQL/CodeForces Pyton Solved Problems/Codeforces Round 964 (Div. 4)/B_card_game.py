# B - Card Game

def is_suneet_gonna_win_in_first_way(a: list[int], b: list[int]) -> str:
    suneet_win_count, opp_win_count = 0, 0

    if a[0] > b[0]:
        suneet_win_count += 1
    
    elif b[0] > a[0]:
        opp_win_count += 1
    
    else:
        pass

    if a[1] > b[1]:
        suneet_win_count += 1

    elif b[1] > a[1]:
        opp_win_count += 1
    
    else:
        pass
    
    if suneet_win_count > opp_win_count:
        return 'won'

    elif opp_win_count > suneet_win_count:
        return 'lost'

    else:
        return 'draw'
    
def is_suneet_gonna_win_in_second_way(a: list[int], b: list[int]) -> str:
    suneet_win_count, opp_win_count = 0, 0

    if a[0] > b[1]:
        suneet_win_count += 1

    elif b[1] > a[0]:
        opp_win_count += 1

    else:
        pass

    if a[1] > b[0]:
        suneet_win_count += 1

    elif b[0] > a[1]:
        opp_win_count += 1

    else:
        pass
    
    if suneet_win_count > opp_win_count:
        return 'won'

    elif opp_win_count > suneet_win_count:
        return 'lost'
    
    else:
        return 'draw'

def is_suneet_gonna_win_in_third_way(a: list[int], b: list[int]) -> str:
    suneet_win_count, opp_win_count = 0, 0

    if a[1] > b[1]:
        suneet_win_count += 1
    
    elif b[1] > a[1]:
        opp_win_count += 1
    
    else:
        pass


    if a[0] > b[0]:
        suneet_win_count += 1
    
    elif b[0] > a[0]:
        opp_win_count += 1
    
    else:
        pass

    if suneet_win_count > opp_win_count:
        return 'won'
    
    elif opp_win_count > suneet_win_count:
        return 'lost'
    
    else:
        return 'draw'

def is_suneet_gonna_win_in_fourth_way(a: list[int], b: list[int]) -> str:
    suneet_win_count, opp_win_count = 0, 0

    if a[1] > b[0]:
        suneet_win_count += 1
    
    elif b[0] > a[1]:
        opp_win_count += 1
    
    else:
        pass

    if a[0] > b[1]:
        suneet_win_count += 1
    
    elif b[1] > a[0]:
        opp_win_count += 1

    else:
        pass
    
    if suneet_win_count > opp_win_count:
        return 'won'
    
    elif opp_win_count > suneet_win_count:
        return 'lost'
    
    else:
        return 'draw'

t = int(input().strip())

for _ in range(t):
    test_input = input().strip().split()
    cards_of_suneet = [int(test_input[0]), int(test_input[1])]
    cards_of_slavic = [int(test_input[2]), int(test_input[3])]

    possible_results = [
        is_suneet_gonna_win_in_first_way(cards_of_suneet, cards_of_slavic),
        is_suneet_gonna_win_in_second_way(cards_of_suneet, cards_of_slavic),
        is_suneet_gonna_win_in_third_way(cards_of_suneet, cards_of_slavic),
        is_suneet_gonna_win_in_fourth_way(cards_of_suneet, cards_of_slavic)
    ]
    print(possible_results.count('won'))