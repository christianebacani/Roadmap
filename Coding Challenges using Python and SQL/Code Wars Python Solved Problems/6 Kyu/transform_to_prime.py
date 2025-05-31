# Question: Transform To Prime
# Categories: 6 Kyu

def minimum_number(numbers: list[int]) -> int:
    total_sum = sum(numbers)
    original_sum = total_sum

    while True:
        if total_sum == 1:
            total_sum += 1
            continue

        elif total_sum == 2:
            break
    
        else:
            pass
            
        prime = True

        for j in range(2, total_sum):
            if total_sum % j == 0:
                prime = False
                break
        
        if prime:
            break

        else:
            total_sum += 1
    
    return abs(original_sum - total_sum)