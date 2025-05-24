# Question: Spot the Differences
# Categories: 7 Kyu

def spot_diff(s1: str, s2: str) -> list[int]:
    return [i for i in range(len(s1)) if s1[i] != s2[i]]