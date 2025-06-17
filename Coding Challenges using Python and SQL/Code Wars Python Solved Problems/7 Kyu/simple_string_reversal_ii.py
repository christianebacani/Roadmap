# Question: Simple string reversal II
# Categories: 7 Kyu

def solve(st: str, a: int, b: int) -> str:
    reversed_portion = st[a:b + 1][::-1]
    st = st[:a] + reversed_portion + st[b + 1:]
    return st