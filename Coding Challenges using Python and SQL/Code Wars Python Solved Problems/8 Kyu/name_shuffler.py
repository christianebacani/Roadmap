# Question: Name Shuffler
# Categories: 8 Kyu

def name_shuffler(str_: str) -> str:
    first_name = str_.split()[0]
    last_name = str_.split()[1]

    return last_name + ' ' + first_name