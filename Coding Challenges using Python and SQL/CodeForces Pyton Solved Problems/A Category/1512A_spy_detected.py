# 1512A - Spy Detected!

t = int(input().strip())

for _ in range(t):
    number_of_elements = input()
    arr = input().strip().split()
    arr = [int(num) for num in arr]

    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            print(i + 1)
            break