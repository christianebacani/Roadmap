# 141A - Amusing Joke

guestname = input().strip()
hostname = input().strip()
letters_in_pile = input().strip()

letters_in_pile_can_be_permutated = True

for i in range(len(guestname)):
    if guestname[i] not in letters_in_pile:
        letters_in_pile_can_be_permutated = False
        break
        
    index_to_remove = letters_in_pile.index(guestname[i])
    letters_in_pile = letters_in_pile[:index_to_remove] + letters_in_pile[index_to_remove + 1:]

for i in range(len(hostname)):
    if hostname[i] not in letters_in_pile:
        letters_in_pile_can_be_permutated = False
        break

    index_to_remove = letters_in_pile.index(hostname[i])
    letters_in_pile = letters_in_pile[:index_to_remove] + letters_in_pile[index_to_remove + 1:]

if letters_in_pile_can_be_permutated and letters_in_pile == '':
    print('YES')

else:
    print('NO')