# 1926A - Vlad and the Best of Five

t = int(input().strip())

for _ in range(t):
    vladislav_string = input().strip()

    if vladislav_string.count('A') > vladislav_string.count('B'):
        print('A')
    
    else:
        print('B')