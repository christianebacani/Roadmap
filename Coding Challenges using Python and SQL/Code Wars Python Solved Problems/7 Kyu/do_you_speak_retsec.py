# Question: Do you speak retsec?
# Categories: 7 Kyu

def reverse_by_center(s: str) -> str:
    if len(s) % 2 == 0:
        index_delimiter = len(s) // 2
        first_half = s[:index_delimiter]
        second_half = s[index_delimiter:]

        answer = second_half + first_half
    
    else:
        index_delimiter = len(s) // 2
        first_half = s[:index_delimiter]
        second_half = s[index_delimiter + 1:]

        answer = second_half + s[index_delimiter] + first_half
    
    return answer