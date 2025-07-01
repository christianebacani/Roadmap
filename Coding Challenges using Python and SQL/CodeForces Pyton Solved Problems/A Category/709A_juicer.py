# 709A - Juicer

test_input = input().strip().split()
n = int(test_input[0])
b = int(test_input[1])
d = int(test_input[2])

sizes = input().strip().split()
sizes = [int(size) for size in sizes]
oranges_in_juicer = []

answer = 0

for i in range(len(sizes)):
    if sizes[i] <= b:
        oranges_in_juicer.append(sizes[i])

    if sum(oranges_in_juicer) > d:
        answer += 1
        oranges_in_juicer = []

print(answer)