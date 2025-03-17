# 2485.) Find the Pivot Integer
# Categories: Math, Prefix Sum

def pivotInteger(n: int) -> int:
    for i in range(1, n + 1):
        x = i
        sum_of_1_to_x = sum(range(1, x + 1))
        sum_of_x_to_n = sum(range(x, n + 1))
        
        if sum_of_1_to_x == sum_of_x_to_n:
            return x

    return -1


