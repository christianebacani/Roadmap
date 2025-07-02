# 1997A - Strong Password

def total_time_to_type_password(password: str) -> int:
    stack = []
    total = 0

    for i in range(len(password)):
        if i == 0:
            total += 2
            stack.append(password[i])
            continue

        if stack[-1] == password[i]:
            total += 1
    
        else:
            total += 2
        
        stack.append(password[i])

    return total

t = int(input().strip())

for _ in range(t):
    s = input().strip()

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_password_and_total_time = {}

    for i in range(len(s)):
        if i == len(s) - 1:
            for j in range(len(alphabet)):
                new_password_and_total_time[s[:i] + alphabet[j] + s[i]] = total_time_to_type_password(s[:i] + alphabet[j] + s[i:])
                new_password_and_total_time[s[:i + 1] + alphabet[j]] = total_time_to_type_password(s[:i + 1] + alphabet[j])
        
        else:
            for j in range(len(alphabet)):
                new_password_and_total_time[s[:i] + alphabet[j] + s[i:]] = total_time_to_type_password(s[:i] + alphabet[j] + s[i:])
    
    maximum_time = max(list(new_password_and_total_time.values()), default=0)

    for new_password, total_time in new_password_and_total_time.items():
        if maximum_time == total_time:
            print(new_password)
            break