# Question: Two Sum
# Categories: 6 Kyu

def two_sum(numbers: list[int], target: int) -> tuple:
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] + numbers[j] == target:
                return tuple([i, j])