# 510A - Fox and Snake

user_input = input().strip().split()
n = int(user_input[0])
m = int(user_input[1])
snake = []

for i in range(n):
    row = []

    for _ in range(m):
        row.append('#')
    
    snake.append(row)

for i in range(len(snake)):
    if (i + 1) % 2 == 0:
        for j in range(len(snake[i])):
            snake[i][j] = '.'

for i in range(len(snake)):
    if (i + 1) % 2 != 0:
        continue

    if i + 1 == 2:
        snake[i][-1] = '#'
        continue
    
    previous_row = snake[i - 2]

    if previous_row[-1] == '#':
        snake[i][0] = '#'
    
    else:
        snake[i][-1] = '#'
    
for i in range(len(snake)):
    print(''.join(snake[i]))