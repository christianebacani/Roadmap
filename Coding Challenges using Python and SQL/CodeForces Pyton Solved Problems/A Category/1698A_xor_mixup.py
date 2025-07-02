# 1698A - XOR Mixup

def bitwise_xor_total(arr: list[int]) -> int:
    total = arr[0]

    for i in range(1, len(arr)):
        total ^= arr[i]
    
    return total

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = input().strip().split()
    a = [int(num) for num in a]
    
    for i in range(len(a)):
        if i == 0:
            elements = a[i + 1:]
        
        elif i == len(a) - 1:
            elements = a[:i]
        
        else:
            elements = a[:i] + a[i + 1:]
        
        if bitwise_xor_total(elements) != a[i]:
            continue

        x = a[i]
        break

    answer = x
    print(answer)