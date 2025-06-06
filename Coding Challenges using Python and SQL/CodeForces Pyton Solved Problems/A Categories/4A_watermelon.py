# 4A - Watermelon

weight = int(input())
weight_can_divide_evenly = False

for i in range(1, weight + 1):
    pete_shares = i
    billy_shares = weight - i

    if pete_shares == 0 or billy_shares == 0:
        continue

    if pete_shares % 2 == 0 and billy_shares % 2 == 0:
        weight_can_divide_evenly = True
        break

if weight_can_divide_evenly:
    print('YES')

else:
    print('NO')