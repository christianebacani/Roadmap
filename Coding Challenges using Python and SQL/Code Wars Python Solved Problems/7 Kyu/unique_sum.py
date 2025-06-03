# Question: Unique Sum
# Categories: 7 Kyu

def unique_sum(lst: list[int]) -> int:
    if lst == []:
        return None

    return sum(list(set(lst)))