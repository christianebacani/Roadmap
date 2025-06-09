# 705A - Hulk

n = int(input().strip())
result = []

for i in range(1, n + 1):
    if i % 2 != 0:
        result.append('I hate')
    
    else:
        result.append('I love')

result = ' that '.join(result)
result = result + ' it'
print(result)