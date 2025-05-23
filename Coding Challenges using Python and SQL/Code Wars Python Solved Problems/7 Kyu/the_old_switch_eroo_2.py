# Question: The old switcheroo 2
# Categories: 7 Kyu

def encode(st: str) -> str:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    st = list(st)

    for i in range(len(st)):
        if st[i].isalpha():
            st[i] = str(alphabets.index(st[i].lower()) + 1)
    
    return ''.join(st)