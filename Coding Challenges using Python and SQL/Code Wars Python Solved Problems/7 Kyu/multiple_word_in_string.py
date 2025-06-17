# Question: Multiple Word in String
# Categories: 7 Kyu

def modify_multiply(st: str, loc: int, num: int) -> str:
    words = st.split()
    multiplied_words = []

    for _ in range(num):
        multiplied_words.append(words[loc])
    
    multiplied_words = '-'.join(multiplied_words)
    return multiplied_words