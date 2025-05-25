# Question: A string of Sorts
# Categories: 6 Kyu

def sort_string(s: str, ordering: str) -> str:
    ordering_list = []
    
    for i in range(len(ordering)):
        if ordering[i] not in ordering_list:
            ordering_list.append(ordering[i])
    
    ordering = ''.join(ordering_list)
    result = ''

    for i in range(len(ordering)):
        for j in range(len(s)):
            if ordering[i] == s[j]:
                result += s[j]
    
    for i in range(len(s)):
        if s[i] not in ordering:
            result += s[i]

    return result