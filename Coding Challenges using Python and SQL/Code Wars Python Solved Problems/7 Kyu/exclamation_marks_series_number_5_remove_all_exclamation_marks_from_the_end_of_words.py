# Question: Exclamation marks series #5: Remove all exclamation marks from the end of words
# Categories: 7 Kyu

def remove(st: str) -> str:
    st = st.split()

    for i in range(len(st)):
        word = st[i][::-1]

        while True:
            if word[0] == '!':
                word = word[1:]
            
            else:
                break
        
        st[i] = word[::-1]

    st = ' '.join(st)
    answer = st

    return answer