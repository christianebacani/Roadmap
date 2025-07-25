# Question: Swapping Cards
# Categories: 7 Kyu

def swap_cards(n1: int, n2: int) -> bool:
    pauls_first_digit = str(n1)[0]
    pauls_second_digit = str(n1)[1]

    opp_first_digit = str(n2)[0]
    opp_second_digit = str(n2)[1]

    if pauls_first_digit <= pauls_second_digit:
        n1 = int(opp_first_digit + str(n1)[1])
        n2 = int(pauls_first_digit + str(n2)[1])
    
    else:
        n1 = int(pauls_first_digit + str(n2)[0])
        n2 = int(pauls_second_digit + str(n2)[1])
    
    if n1 > n2:
        return True
    
    return False