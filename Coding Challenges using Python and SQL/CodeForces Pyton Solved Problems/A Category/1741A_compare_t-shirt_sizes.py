# 1741A - Compare T-Shirt Sizes

t = int(input().strip())

for _ in range(t):
    tshirt_sizes = input().strip().split()
    a = tshirt_sizes[0]
    b = tshirt_sizes[1]

    if a == b:
        print('=')
        continue

    if a[-1] == 'S' and b[-1] != 'S':
        print('<')
    
    elif a[-1] != 'S' and b[-1] == 'S':
        print('>')
    
    elif a[-1] == 'L' and b[-1] != 'L':
        print('>')

    elif a[-1] != 'L' and b[-1] == 'L':
        print('<')
        
    elif (a[-1] == 'S' and b[-1] == 'S') and (a.count('X') > b.count('X')):
        print('<')
    
    elif (a[-1] == 'S' and b[-1] == 'S') and (a.count('X') < b.count('X')):
        print('>')
    
    elif (a[-1] == 'L' and b[-1] == 'L') and (a.count('X') > b.count('X')):
        print('>')
    
    else:
        print('<')