# Question: Find The Duplicated Number in a Consecutive Unsorted List
# Categories: 7 Kyu

def find_dup(arr: list[int]) -> int:
    for number in range(min(arr), max(arr) + 1):
        if arr.count(number) > 1:
            return number