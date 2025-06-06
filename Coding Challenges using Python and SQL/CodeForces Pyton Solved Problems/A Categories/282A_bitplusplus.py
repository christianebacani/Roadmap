# 282A - Bit++

number_of_commands = int(input())
x = 0

for _ in range(number_of_commands):
    command = input().strip()

    if '++' in command:
        x += 1

    else:
        x -= 1

print(x)