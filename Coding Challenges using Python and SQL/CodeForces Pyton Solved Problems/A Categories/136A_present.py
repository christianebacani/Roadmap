# 136A - Presents

n = int(input().strip())
p = input().strip().split()
result = []

for i in range(len(p)):
    p[i] = int(p[i])

for i in range(1, len(p) + 1):
    target_index = p.index(i) + 1
    result.append(str(target_index))

answer = ' '.join(result)
print(answer)