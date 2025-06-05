# Question: Convert boolean values to string 'Yes' or 'No'
# Categories: 8 Kyu

def bool_to_word(boolean: bool) -> str:
    if boolean is True:
        return 'Yes'
    
    return 'No'