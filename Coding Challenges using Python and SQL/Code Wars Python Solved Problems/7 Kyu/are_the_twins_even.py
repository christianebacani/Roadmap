# Question: Are the twins even?
# Categories: 7 Kyu

def even_twins(numbers: list[int]) -> int:
    sums = []

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i < j:
                sums.append(numbers[i] + numbers[j])
    
    sums = list(set(sums))
    count = 0

    for i in range(len(sums)):
        if sums[i] % 2 == 0:
            count += 1
    
    return count