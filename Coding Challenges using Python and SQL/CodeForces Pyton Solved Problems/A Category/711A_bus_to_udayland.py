# 711A - Bus to Udayland

rows = int(input().strip())
bus_seats = []

for _ in range(rows):
    bus_seats.append(input().strip())

they_seat_in_neighboring_empty_seat = False

for i in range(len(bus_seats)):
    if bus_seats[i][:2] == 'OO':
        they_seat_in_neighboring_empty_seat = True
        bus_seats[i] = '++|' + bus_seats[i][3:]
        break

    if bus_seats[i][3:] == 'OO':
        they_seat_in_neighboring_empty_seat = True
        bus_seats[i] = bus_seats[i][:2] + '|++'
        break

if they_seat_in_neighboring_empty_seat:
    print('YES')

    for i in range(len(bus_seats)):
        print(bus_seats[i])

else:
    print('NO')