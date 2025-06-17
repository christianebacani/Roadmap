# 1971A - My First Sorting Problem

t = int(input().strip())

for _ in range(t):
    arr = input().strip().split()
    arr = [int(num) for num in arr]

    print(f'{min(arr)} {max(arr)}')