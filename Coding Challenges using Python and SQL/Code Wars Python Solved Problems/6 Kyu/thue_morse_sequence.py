# Question: Thue-Morse Sequence
# Categories: 6 Kyu

def thue_morse(n: int) -> str:
    thue_morse_sequence = '0'

    while len(thue_morse_sequence) < 10000:
        reverse_thue_morse_sequence = ''

        for i in range(len(thue_morse_sequence)):
            if thue_morse_sequence[i] == '1':
                reverse_thue_morse_sequence += '0'
            
            else:
                reverse_thue_morse_sequence += '1'
        
        thue_morse_sequence = thue_morse_sequence + reverse_thue_morse_sequence

    return thue_morse_sequence[:n]