# 228A - Is your horseshoe on the other hoof?

colors = input().strip().split()
answer = len(colors) - len(set(colors))
print(answer)