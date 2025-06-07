# 266A - Stones on the Table

number_of_stones = int(input().strip())
color_of_stones = list(input())
count = 0

for i in range(1, len(color_of_stones)):
    if color_of_stones[i - 1] == color_of_stones[i]:
        count += 1

answer = count
print(answer)