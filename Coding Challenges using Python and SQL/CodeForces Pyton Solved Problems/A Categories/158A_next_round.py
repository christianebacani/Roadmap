# 158A - Next Round

kth_place = int(input().split()[1])
contestants = input().split()
threshold = 0

for i in range(len(contestants)):
    contestants[i] = int(contestants[i])

for index, contestant in enumerate(contestants):
    index += 1

    if index == kth_place:
        threshold = contestant
        break

count = 0

for contestant in contestants:
    if contestant <= 0:
        continue

    if contestant >= threshold:
        count += 1

answer = count
print(answer)