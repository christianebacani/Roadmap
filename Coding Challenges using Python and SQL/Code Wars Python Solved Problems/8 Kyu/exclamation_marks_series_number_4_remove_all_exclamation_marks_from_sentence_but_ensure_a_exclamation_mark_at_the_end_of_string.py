# Question: Exclamation marks series #4: Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string
# Categories: 8 Kyu

def remove(st: str) -> str:
    st = st.replace('!', '')
    st = st + '!'
    answer = st

    return answer