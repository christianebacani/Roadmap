# 1633A - Div. 7

t = int(input().strip())

for _ in range(t):
    n = input().strip()

    if int(n) % 7 == 0:
        print(n)
        continue
    
    digits = '0123456789'

    for i in range(len(n)):
        the_changes_was_implemented = False
        digit = n[i]
        
        for j in range(len(digits)):
            if int(n[:i] + digits[j] + n[i + 1:]) % 7 != 0:
                continue
            
            if (n[:i] + digits[j] + n[i + 1:])[0] == '0':
                continue

            digit = digits[j]
            the_changes_was_implemented = True
            break
    
        if the_changes_was_implemented:
            n = n[:i] + digit + n[i + 1:]
            break
    
    print(int(n))