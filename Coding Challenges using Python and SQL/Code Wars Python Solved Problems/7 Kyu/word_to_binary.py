# Question: Word to binary
# Categories: 7 Kyu

def word_to_bin(word: str) -> list[str]:
    list_of_binaries = []

    for i in range(len(word)):
        ascii_code = ord(word[i])
        binary = bin(ascii_code)[2:]

        if len(binary) != 8:
            prefix = (8 - len(binary)) * '0'
            binary = prefix + binary
        
        list_of_binaries.append(binary)

    return list_of_binaries