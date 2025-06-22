# 124A - The number of positions

test_input = input().strip().split()
n = int(test_input[0])
a = int(test_input[1])
b = int(test_input[2])

line = []

for i in range(1, n + 1):
    line.append(i)

count = 0

for i in range(len(line)):
    people_in_front_of_him = line[:i]
    people_behind_him = line[i + 1:]

    if len(people_in_front_of_him) >= a and len(people_behind_him) <= b:
        count += 1

print(count)