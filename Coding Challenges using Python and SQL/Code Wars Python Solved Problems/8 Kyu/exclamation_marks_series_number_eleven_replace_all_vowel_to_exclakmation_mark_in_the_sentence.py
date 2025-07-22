# Question: Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence
# Categories: 8 Kyu

def replace_exclamation(st: str) -> str:
    vowels = 'aeiouAEIOU'
    
    for i in range(len(vowels)):
        if vowels[i] in st:
            st = st.replace(vowels[i], '!')

    return st