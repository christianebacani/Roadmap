# 1095A - Repeating Cipher

n = int(input().strip())
s = input().strip()
repetitions = []

for i in range(1, 10 + 1):
    if (sum(repetitions) + i) <= n:
        repetitions.append(i)
        continue

    break

answer = ''

for i in range(len(repetitions)):
    answer += ''.join(list(set(s[:repetitions[i]])))
    s = s[repetitions[i]:]

print(answer)