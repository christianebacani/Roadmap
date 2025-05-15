# Question: Abbreviate a Two Word Name
# Categories: 8 Kyu

def abbrev_name(name: str) -> str:
    name = name.split()
    first_initial = name[0].capitalize()[0]
    second_initial = name[1].capitalize()[0]

    return f'{first_initial}.{second_initial}'