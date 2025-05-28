# Question: Password Check - Binary to String
# Categories: 7 Kyu

def decode_pass(list_of_possible_passwords: list[str], binaries: str) -> str | bool:
    binaries = binaries.split()
    decoded_binaries = ''

    for i in range(len(binaries)):
        ascii_code = int(binaries[i], 2)
        ascii_character = chr(ascii_code)
        decoded_binaries += ascii_character
    
    if decoded_binaries in list_of_possible_passwords:
        return decoded_binaries
    
    return False