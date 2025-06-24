# 1607A - Linear Keyboard

t = int(input().strip())

for _ in range(t):
    keyboard = input().strip()
    s = input().strip()    
    total_units = 0

    if len(s) == 1:
        print(total_units)
        continue
    
    for i in range(1, len(s)):
        previous_letter = s[i - 1]
        current_letter = s[i]

        total_units += abs((keyboard.index(previous_letter) + 1) - (keyboard.index(current_letter) + 1))

    print(total_units)