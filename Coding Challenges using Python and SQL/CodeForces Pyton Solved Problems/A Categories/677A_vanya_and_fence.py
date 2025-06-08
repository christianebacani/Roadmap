# 677A - Vanya and Fence

user_input = input().strip().split()
length_of_fence = int(user_input[1])

list_of_height = input().strip().split()

for i in range(len(list_of_height)):
    list_of_height[i] = int(list_of_height[i])

width = 0

for i in range(len(list_of_height)):
    if list_of_height[i] <= length_of_fence:
        width += 1
    
    else:
        width += 2

answer = width
print(answer)