# Question: Head, Tail, Init and Last
# Categories: 7 Kyu

def head(arr: list[int]) -> int:
    return arr[0]

def tail(arr: list[int]) -> list[int]:
    return arr[1:]

def init(arr: list[int]) -> list[int]:
    return arr[:-1]

def last(arr: list[int]) -> int:
    return arr[-1]