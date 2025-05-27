# Question: Help Bob count letters and digits
# Categories: 7 Kyu

def count_letters_and_digits(s: str) -> int:
    count = 0

    for i in range(len(s)):
        if s[i].isalnum():
            count += 1

    return count