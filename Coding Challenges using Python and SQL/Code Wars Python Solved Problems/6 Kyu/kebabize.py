# Question: Kebabize
# Categories: 6 Kyu

def kebabize(st: str) -> str:
    digits = '0123456789'

    for i in range(len(digits)):
        st = st.replace(digits[i], '')
    
    formatted_st = ''

    for i in range(len(st)):
        if st[i].isupper():
            formatted_st += ' '
        
        formatted_st += st[i].lower()
    
    return '-'.join(formatted_st.split())