# A - Nezha Naohai

user_input = input().strip().split()
hours_of_disturbances = user_input[:3]
hours_of_disturbances = [int(hours) for hours in hours_of_disturbances]
d = int(user_input[3])
total = 0

for i in range(len(hours_of_disturbances)):
    total += (d * hours_of_disturbances[i])

answer = total
print(answer)