# Question: Case-sensitive!
# Categories: 7 Kyu

def case_sensitive(s: str) -> list[bool, list[str]]:
    letters_all_lowercase = True
    letters_that_are_uppercase = []

    for i in range(len(s)):
        if s[i].isupper():
            letters_all_lowercase = False
            letters_that_are_uppercase.append(s[i])

    return [letters_all_lowercase, letters_that_are_uppercase]