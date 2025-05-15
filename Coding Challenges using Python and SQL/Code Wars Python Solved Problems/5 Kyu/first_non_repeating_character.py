# Question: First non-repeating character
# Categories: 5 Kyu

def first_non_repeating_letter(s: str) -> str:
    copied_string = s
    strng = s.lower()

    for i in range(len(strng)):
        if strng.count(strng[i]) == 1:
            return copied_string[i]

    return ''