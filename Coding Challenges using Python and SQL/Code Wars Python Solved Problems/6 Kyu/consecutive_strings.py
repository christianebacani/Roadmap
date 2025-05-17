# Question: Consecutive strings
# Categories: 6 Kyu

def longest_consec(strarr: list[str], k: int) -> str:
    if (strarr == []) or (k <= 0) or (k > len(strarr)):
        return ''

    consecutive_strings = []
    
    for i in range(len(strarr)):
        consecutive_string = strarr[i : i + k]

        if len(consecutive_string) == k:
            consecutive_strings.append(''.join(consecutive_string))
    
    maximum_length = 0

    for i in range(len(consecutive_strings)):
        if len(consecutive_strings[i]) > maximum_length:
            maximum_length = len(consecutive_strings[i])
    
    for i in range(len(consecutive_strings)):
        if maximum_length == len(consecutive_strings[i]):
            return consecutive_strings[i]