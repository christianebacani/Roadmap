# A - Wrong Subtraction

user_input = input().strip().split()
n = int(user_input[0])
k = int(user_input[1])

for _ in range(k):
    if int(str(n)[-1]) != 0:
        n -= 1
    
    else:
        n = n // 10

print(n)