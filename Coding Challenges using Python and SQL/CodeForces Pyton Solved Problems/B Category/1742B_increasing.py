# 1742B - Increasing

t = int(input().strip())

for _ in range(t):
    n = input().strip()
    arr = input().strip().split()
    arr = [int(num) for num in arr]
    arr.sort()

    is_arr_strictly_increasing = True

    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            is_arr_strictly_increasing = False
            break
    
    if is_arr_strictly_increasing:
        print('YES')
    
    else:
        print('NO')