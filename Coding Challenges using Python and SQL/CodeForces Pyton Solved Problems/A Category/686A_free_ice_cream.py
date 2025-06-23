# 686A - Free Ice Cream

test_input = input().strip().split()
n = int(test_input[0])
x = int(test_input[1])

queue = []

for _ in range(n):
    queue.append(input().strip().split())

number_of_ice_cream_packs = x
number_of_distressed_kids = 0

for i in range(len(queue)):
    if queue[i][0] == '+':
        number_of_ice_cream_packs += int(queue[i][1])
        continue

    if number_of_ice_cream_packs >= int(queue[i][1]):
        number_of_ice_cream_packs -= int(queue[i][1])
    
    else:
        number_of_distressed_kids += 1

print(f'{number_of_ice_cream_packs} {number_of_distressed_kids}')