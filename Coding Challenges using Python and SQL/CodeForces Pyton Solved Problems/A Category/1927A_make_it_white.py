# 1927A - Make it White

t = int(input().strip())

for _ in range(t):
    n = input()
    horizontal_strip = input().strip()

    length_of_subsequence_containing_black_strip = []

    for i in range(1, len(horizontal_strip) + 1):
        for j in range(len(horizontal_strip)):
            subsequence = horizontal_strip[j : j + i]

            if len(subsequence) != i:
                continue

            if 'B' not in subsequence:
                continue

            if 'B' in horizontal_strip[:j] or 'B' in horizontal_strip[j + i:]:
                continue

            length_of_subsequence_containing_black_strip.append(len(subsequence))
        
    print(min(length_of_subsequence_containing_black_strip, default=0))