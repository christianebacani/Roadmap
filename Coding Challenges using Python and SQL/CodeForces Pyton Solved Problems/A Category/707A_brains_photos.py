# 707A - Brain's Photos

user_input = input().strip().split()
n = int(user_input[0])
m = int(user_input[1])
photos = []

for _ in range(n):
    row = input().strip().split()
    photos.append(row)

photo_is_all_black_and_white = True
colored_pixels = 'CMY'

for i in range(len(colored_pixels)):
    for j in range(len(photos)):
        if colored_pixels[i] in photos[j]:
            photo_is_all_black_and_white = False
            break

if photo_is_all_black_and_white:
    print('#Black&White')

else:
    print('#Color')