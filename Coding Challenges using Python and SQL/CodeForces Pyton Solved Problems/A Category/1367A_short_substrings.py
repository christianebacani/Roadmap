# 1367A - Short Substrings

t = int(input().strip())

for i in range(t):
    b = input().strip()
    answer = ''

    for i in range(0, len(b), 2):
        substring = b[i:i + 2]
        
        if answer == '' or answer[-1] != substring[0]:
            answer += substring[0]
        
        answer += substring[1]
    
    print(answer)