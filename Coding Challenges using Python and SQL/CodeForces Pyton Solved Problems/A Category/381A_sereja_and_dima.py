# 381A - Sereja and Dima

n = input()
cards = input().strip().split()
cards = [int(card) for card in cards]
total_cards = len(cards)

cards_of_sereja = []
cards_of_dima = []

for i in range(total_cards):
    if len(cards) == 1:
        chosen_card = cards[0]

    elif cards[0] > cards[-1]:
        chosen_card = cards[0]
        cards = cards[1:]

    elif cards[-1] > cards[0]:
        chosen_card = cards[-1]
        cards = cards[:-1]

    if i % 2 == 0:
        cards_of_sereja.append(chosen_card)

    else:
        cards_of_dima.append(chosen_card)

print(f'{sum(cards_of_sereja)} {sum(cards_of_dima)}')