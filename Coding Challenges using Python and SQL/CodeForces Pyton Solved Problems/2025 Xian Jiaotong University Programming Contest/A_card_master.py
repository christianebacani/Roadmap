# A - Card Master

cards = input().strip().split()
cards = [int(card) for card in cards]

if len(set(cards)) == 1:
    print(sum(cards) + 100)

else:
    print(sum(cards))