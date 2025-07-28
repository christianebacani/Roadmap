# Question: Regex count lowercase letters
# Categories: 8 Kyu

def lowercase_count(strng: str) -> str:
    total = 0

    for i in range(len(strng)):
        if strng[i].islower() and strng[i].isalpha():
            total += 1

    return total