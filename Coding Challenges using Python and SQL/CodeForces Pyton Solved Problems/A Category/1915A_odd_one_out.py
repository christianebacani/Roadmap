# 1915A - Odd One Out

t = int(input().strip())

for _ in range(t):
    arr = input().strip().split()
    arr = [int(num) for num in arr]

    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            print(arr[i])
            break