# Question: Twisted Sum
# Categories: 6 Kyu

def compute_sum(n: int) -> str:
    total = 0

    for i in range(1, n + 1):
        if len(str(i)) > 1:
            sum_of_digits = 0

            for j in range(len(str(i))):
                sum_of_digits += int(str(i)[j])

            total += sum_of_digits

        else:
            total += i
    
    return total