# 1760A - Medium Number

t = int(input().strip())

for _ in range(t):
    distinct_integers = input().strip().split()
    distinct_integers = [int(num) for num in distinct_integers]
    distinct_integers.sort()

    print(distinct_integers[1])