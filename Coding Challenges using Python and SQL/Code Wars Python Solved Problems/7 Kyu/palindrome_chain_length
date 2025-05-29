# Question: Palindrome chain length
# Categories: 7 Kyu

def palindrome_chain_length(n: int) -> int:
    string_number = str(n)
    steps = 0

    while string_number != string_number[::-1]:
        reversed_string_number = int(string_number[::-1])
        string_number = str(int(string_number) + reversed_string_number)
        steps += 1
    
    return steps