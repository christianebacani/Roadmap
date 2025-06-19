# 1915B - Not Quite Latin Square

t = int(input().strip())

for _ in range(t):
    squares = []
    
    for _ in range(3):
        squares.append(input().strip())
    
    letters = 'ABC'

    for i in range(len(squares)):
        if '?' not in squares[i]:
            continue

        missing_letter_found = False
        missing_letter = None

        for j in range(len(letters)):
            if letters[j] in squares[i]:
                continue
            
            missing_letter = letters[j]
            missing_letter_found = True
            break
    
        if missing_letter_found:
            print(missing_letter)
            break