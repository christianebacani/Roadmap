# Question: Zero Terminated Sum
# Categories: 7 Kyu

def largest_sum(s: str) -> int:
    s = s.replace('0', ' ')
    s = s.split()

    if s == []:
        return 0

    sum_of_digits_substring = []

    for i in range(len(s)):
        total = 0

        for j in range(len(s[i])):
            total += int(s[i][j])
        
        sum_of_digits_substring.append(total)
    
    return max(sum_of_digits_substring)