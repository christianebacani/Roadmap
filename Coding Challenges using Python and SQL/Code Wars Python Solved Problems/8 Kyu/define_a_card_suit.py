# Question: Define a card suit
# Categories: 8 Kyu

def define_suit(card: str) -> str:
    if card[-1] == 'C':
        return 'clubs'
    
    elif card[-1] == 'S':
        return 'spades'
    
    elif card[-1] == 'D':
        return 'diamonds'
    
    else:
        return 'hearts'