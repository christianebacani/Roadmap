# 791A - Bear and Big Brother

user_input = input().strip().split()
limak_weight = int(user_input[0])
bob_weight = int(user_input[1])
years = 0

while True:
    if limak_weight <= bob_weight:
        years += 1
        limak_weight = limak_weight * 3
        bob_weight = bob_weight * 2
    
    else:
        break

print(years)