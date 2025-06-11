# 427A - Police Recruits

n = input().strip()
crimes_or_new_recruit = input().strip().split()
crimes_or_new_recruit = [int(num) for num in crimes_or_new_recruit]

available_police = 0
crimes_unsolved = 0

for i in range(len(crimes_or_new_recruit)):
    if crimes_or_new_recruit[i] > 0:
        available_police += crimes_or_new_recruit[i]
        continue

    if available_police > 0:
        available_police -= 1
        continue

    crimes_unsolved += 1

print(crimes_unsolved)