# 2106A - Dr. TC

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    s = input().strip()
    list_of_binary_strings = []

    for i in range(len(s)):
        if s[i] == '1':
            flipped_bit = '0'
        
        else:
            flipped_bit = '1'
        
        list_of_binary_strings.append(s[:i] + flipped_bit + s[i + 1:])
    
    total_bits = 0

    for i in range(len(list_of_binary_strings)):
        total_bits += list_of_binary_strings[i].count('1')
    
    answer = total_bits
    print(answer)