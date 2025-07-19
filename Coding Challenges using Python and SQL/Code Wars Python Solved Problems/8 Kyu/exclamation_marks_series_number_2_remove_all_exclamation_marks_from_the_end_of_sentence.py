# Question: Exclamation marks series #2: Remove all exclamation marks from the end of sentence
# Categories: 8 Kyu

def remove(st: str) -> str:
    st = st[::-1]

    while True:
        if st[0] == '!':
            st = st[1:]

        else:
            break

    st = st[::-1]
    answer = st

    return answer