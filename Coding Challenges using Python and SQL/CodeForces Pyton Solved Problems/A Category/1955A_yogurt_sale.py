# 1955A - Yogurt Sale

def total_spent_when_using_regular_price(total_yogurts: int, regular_price: int) -> int:
    return total_yogurts * regular_price

def total_spent_when_using_promotion_price(total_yogurts: int, regular_price: int, promotion_price: int) -> int:
    total_spent = 0

    while total_yogurts > 0:
        if total_yogurts >= 2:
            total_spent += promotion_price
            total_yogurts -= 2
        
        else:
            total_spent += regular_price
            total_yogurts -= 1
    
    return total_spent

t = int(input().strip())

for _ in range(t):
    user_input = input().strip().split()
    n = int(user_input[0])
    a = int(user_input[1])
    b = int(user_input[2])

    if total_spent_when_using_regular_price(n, a) <= total_spent_when_using_promotion_price(n, a, b):
        print(total_spent_when_using_regular_price(n, a))
    
    else:
        print(total_spent_when_using_promotion_price(n, a, b))