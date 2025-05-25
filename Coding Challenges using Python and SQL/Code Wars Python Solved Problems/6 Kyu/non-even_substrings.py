# Question: Non-even substrings
# Categories: 6 Kyu

def solve(s: str) -> int:
    odd_numbers_in_s = []

    for i in range(1, len(s) + 1):
        for j in range(len(s)):
            substring = s[j : j + i]

            if len(substring) != i:
                continue

            if int(substring) % 2 != 0:
                odd_numbers_in_s.append(substring)
    
    return len(odd_numbers_in_s)