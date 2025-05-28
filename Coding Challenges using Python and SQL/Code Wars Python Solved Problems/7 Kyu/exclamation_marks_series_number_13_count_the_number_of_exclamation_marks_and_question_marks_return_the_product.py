# Question: Exclamation marks series #13: Count the number of exclamation marks and question marks, return the product
# Categories: 7 Kyu

def product(st: str) -> int:
    exclamation_mark_count = st.count('!')
    question_mark_count = st.count('?')

    return exclamation_mark_count * question_mark_count