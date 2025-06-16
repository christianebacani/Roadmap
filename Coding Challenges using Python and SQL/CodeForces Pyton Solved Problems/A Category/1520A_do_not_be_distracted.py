# 1520A - Do Not Be Distracted!

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    task = input().strip()

    stack = []
    teacher_is_suspicious = False

    for i in range(len(task)):
        if stack == []:
            stack.append(task[i])
            continue
        
        if task[i] != stack[-1] and task[i] in stack:
            teacher_is_suspicious = True
            break

        stack.append(task[i])

    if not teacher_is_suspicious:
        print('YES')

    else:
        print('NO')