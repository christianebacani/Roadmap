# 2014A - Robin Helps

t = int(input().strip())

for _ in range(t):
    test_input = input().strip().split()
    n = int(test_input[0])
    k = int(test_input[1])

    golds = input().strip().split()
    golds = [int(gold) for gold in golds]

    total_golds_robin_had = 0
    number_of_people_robin_gives_gold = 0

    for i in range(len(golds)):
        if golds[i] >= k:
            total_golds_robin_had += golds[i]
            continue

        if golds[i] != 0:
            continue

        if total_golds_robin_had > 0:
            number_of_people_robin_gives_gold += 1
            total_golds_robin_had -= 1
    
    print(number_of_people_robin_gives_gold)