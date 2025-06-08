# 467A - George and Accomodation

n = int(input().strip())
count = 0

for _ in range(n):
    user_input = input().strip().split()
    number_of_people = int(user_input[0])
    maximum_people = int(user_input[1])

    available_capacity = (maximum_people - number_of_people)

    if available_capacity >= 2:
        count += 1

answer = count
print(answer)