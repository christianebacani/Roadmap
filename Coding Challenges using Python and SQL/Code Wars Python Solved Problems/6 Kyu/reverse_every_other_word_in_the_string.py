# Question: Reverse every other word in the string
# Categories: 6 Kyu

def reverse_alternate(st: str) -> str:
    st = st.split()

    for i in range(len(st)):
        if i % 2 != 0:
            st[i] = st[i][::-1]

    return ' '.join(st)