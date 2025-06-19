# 2065A - Skibidus and Amog'u

t = int(input().strip())

for _ in range(t):
    W = input().strip()
    amogu_noun = W

    amogu_noun = amogu_noun[:-2]
    amogu_noun = amogu_noun + 'i'

    print(amogu_noun)