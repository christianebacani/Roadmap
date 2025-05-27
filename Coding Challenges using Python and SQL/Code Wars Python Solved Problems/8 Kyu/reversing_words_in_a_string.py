# Question: Reversing Words in a String
# Categories: 8 Kyu

def reverse(st: str) -> str:
    return ' '.join(st.split()[::-1])