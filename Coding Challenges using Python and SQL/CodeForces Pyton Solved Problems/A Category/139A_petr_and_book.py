# 139A - Petr and Book

n = int(input().strip())
pages_per_day = input().strip().split()
pages_per_day = [int(page) for page in pages_per_day]

total_pages = 0
answer = None

while True:
    total_pages += pages_per_day[0]

    if total_pages >= n:
        answer = 1
        break

    total_pages += pages_per_day[1]

    if total_pages >= n:
        answer = 2
        break

    total_pages += pages_per_day[2]

    if total_pages >= n:
        answer = 3
        break

    total_pages += pages_per_day[3]

    if total_pages >= n:
        answer = 4
        break

    total_pages += pages_per_day[4]

    if total_pages >= n:
        answer = 5
        break

    total_pages += pages_per_day[5]

    if total_pages >= n:
        answer = 6
        break

    total_pages += pages_per_day[6]

    if total_pages >= n:
        answer = 7
        break

print(answer)