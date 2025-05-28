# Question: noobCode 03: CHECK THESE LETTERS... see if letters in "String 2" are present in "String 1"
# Categories: 7 Kyu

def letter_check(arr: list[str]) -> bool: 
    first_string = arr[0].lower()
    second_string = arr[1].lower()

    for i in range(len(second_string)):
        if second_string[i] not in first_string:
            return False

    return True