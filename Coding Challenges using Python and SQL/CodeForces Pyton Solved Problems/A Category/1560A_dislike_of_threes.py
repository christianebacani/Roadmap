# 1560A - Dislike of Threes

t = int(input().strip())
polycarpus_sequences = []

for i in range(1, 2006):
    if str(i)[-1] != '3' and i % 3 != 0:
        polycarpus_sequences.append(i)

for _ in range(t):
    k = int(input().strip())
    print(polycarpus_sequences[k - 1])