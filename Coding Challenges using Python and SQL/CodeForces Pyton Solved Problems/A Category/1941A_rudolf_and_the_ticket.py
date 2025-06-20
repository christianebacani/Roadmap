# 1941A - Rudolf and the Ticket

t = int(input().strip())

for _ in range(t):
    test_input = input().strip().split()
    n = int(test_input[0])
    m = int(test_input[1])
    k = int(test_input[2])
    
    left_pocket_coins = input().strip().split()
    left_pocket_coins = [int(coin) for coin in left_pocket_coins]

    right_pocket_coins = input().strip().split()
    right_pocket_coins = [int(coin) for coin in right_pocket_coins]

    total_ways = 0

    for i in range(len(left_pocket_coins)):
        for j in range(len(right_pocket_coins)):
            if left_pocket_coins[i] + right_pocket_coins[j] > k:
                continue
            
            total_ways += 1
    
    print(total_ways)