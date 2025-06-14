# Question: String Suffixes
# Categories: 6 Kyu

def string_suffix(str_: str) -> int:
    suffixes = []

    for i in range(len(str_)):
        suffixes.append(str_[i:])

    total = 0

    for i in range(len(suffixes)):
        list_of_length_of_prefixes = []

        reverse_suffix = suffixes[i][::-1]

        for j in range(len(reverse_suffix)):
            if str_.startswith(reverse_suffix[j:][::-1]):
                list_of_length_of_prefixes.append(len(reverse_suffix[j:][::-1]))
        
        total += max(list_of_length_of_prefixes, default=0)
    
    return total