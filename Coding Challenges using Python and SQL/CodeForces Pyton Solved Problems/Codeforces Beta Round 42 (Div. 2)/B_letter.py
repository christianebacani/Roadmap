# B - Letter

headings = input().strip()
text = input().strip()
anonymous_letter = ''

for i in range(len(text)):
    if text[i] == ' ':
        anonymous_letter += ' '
        continue

    for j in range(len(headings)):
        if text[i] == headings[j]:
            anonymous_letter += headings[j]
            headings = headings[:j] + headings[j + 1:]
            break
            
if anonymous_letter == text:
    print('YES')

else:
    print('NO')