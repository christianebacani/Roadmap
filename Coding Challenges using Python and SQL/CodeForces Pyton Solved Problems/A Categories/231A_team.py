# 231A: Team

number_of_questions = int(input())
answer = 0

for _ in range(number_of_questions):
    team = input().split()
    
    petya = int(team[0]) 
    vasya = int(team[1])
    tonya = int(team[2])

    total = petya + vasya + tonya

    if total >= 2:
        answer += 1

print(answer)