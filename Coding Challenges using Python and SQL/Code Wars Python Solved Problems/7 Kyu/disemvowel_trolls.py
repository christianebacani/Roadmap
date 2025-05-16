# Question: Disemvowel Trolls
# Categories: 7 Kyu

def disemvowel(string_: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''

    for i in range(len(string_)):
        if string_[i].lower() in vowels:
            continue

        result += string_[i]
    
    return result