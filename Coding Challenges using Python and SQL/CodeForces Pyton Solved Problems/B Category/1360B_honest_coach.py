# 1360B - Honest Coach

t = int(input().strip())

for _ in range(t):
    n = input()
    strengths = input().strip().split()
    strengths = [int(strength) for strength in strengths]
    strengths.sort()

    differences = []

    for i in range(1, len(strengths)):
        differences.append(abs(strengths[i] - strengths[i - 1]))
    
    minimum_difference = min(differences)
    a, b, = [], []

    for i in range(1, len(strengths)):
        if abs(strengths[i] - strengths[i - 1]) == minimum_difference:
            a = strengths[:i]
            b = strengths[i:]
            break
    
    print(abs(max(a) - min(b)))