# Question: Is there a vowel in there?
# Categories: 8 Kyu

def is_vow(arr: list[int]) -> list[str | int]:
    vowels = 'aeiou'

    for i in range(len(arr)):
        number = arr[i]
        ascii_letter = chr(number)

        if ascii_letter in vowels:
            arr[i] = ascii_letter

    return arr