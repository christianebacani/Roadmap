# Question: String matchup
# Categories: 7 Kyu

def solve(a: list[str], b: list[str]) -> list[int]:
    return [a.count(b[i]) for i in range(len(b))]