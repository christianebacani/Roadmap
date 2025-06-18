# 1760B - Atilla's Favorite Problem

t = int(input().strip())
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for _ in range(t):
    n = input()
    letters = input().strip()
    last_letter = sorted(letters)[-1]

    index = alphabet.index(last_letter)
    print(len(alphabet[:index + 1]))