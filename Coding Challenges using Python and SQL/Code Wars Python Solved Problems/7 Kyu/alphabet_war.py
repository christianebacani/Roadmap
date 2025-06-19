# Question: Alphabet war
# Categories: 7 Kyu

def alphabet_war(fight: str) -> str:
    left_side_powers = {
        'w': 4,
        'p': 3,
        'b': 2,
        's': 1
   }
    right_side_powers = {
        'm': 4,
        'q': 3,
        'd': 2,
        'z': 1
    }
    left_side_total_powers, right_side_total_powers = 0, 0

    for i in range(len(fight)):
        if fight[i] in left_side_powers:
            left_side_total_powers += left_side_powers[fight[i]]
        
        elif fight[i] in right_side_powers:
            right_side_total_powers += right_side_powers[fight[i]]
        
        else:
            pass

    if left_side_total_powers > right_side_total_powers:
        return 'Left side wins!'

    elif right_side_total_powers > left_side_total_powers:
        return 'Right side wins!'

    else:
        return 'Let\'s fight again!'