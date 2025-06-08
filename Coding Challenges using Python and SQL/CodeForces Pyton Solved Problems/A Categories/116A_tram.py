# 116A - Tram

n = int(input().strip())
stack = []

for i in range(n):
    user_input = input().strip().split()
    number_of_passengers_who_exit = int(user_input[0])
    number_of_passengers_who_enter = int(user_input[1])

    if i == 0:
        stack.append(number_of_passengers_who_enter)
        continue
    
    number_of_passenger_in_train = stack[-1]
    stack.append((number_of_passenger_in_train - number_of_passengers_who_exit) + number_of_passengers_who_enter)

print(max(stack))