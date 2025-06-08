# 734A - Anton and Danik

number_of_games = int(input().strip())
results = input().strip()

if results.count('A') > results.count('D'):
    print('Anton')

elif results.count('D') > results.count('A'):
    print('Danik')

else:
    print('Friendship')