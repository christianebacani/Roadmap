# 1703B - ICPC Baloons

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    s = input().strip()

    solved_problems = []
    total_score = 0

    for i in range(len(s)):
        if s[i] not in solved_problems:
            total_score += 2
            solved_problems.append(s[i])
            continue
        
        total_score += 1
    
    print(total_score)