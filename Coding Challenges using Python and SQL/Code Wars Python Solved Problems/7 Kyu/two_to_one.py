# Question: Two to One
# Categories: 7 Kyu

def longest(a1: str, a2: str) -> str:
    merged_string = sorted(a1 + a2)
    merged_string = ''.join(merged_string)
    longest_distinct_substrings = []

    for i in range(len(merged_string)):
        if merged_string[i] not in longest_distinct_substrings:
            longest_distinct_substrings.append(merged_string[i])
    
    return ''.join(longest_distinct_substrings)