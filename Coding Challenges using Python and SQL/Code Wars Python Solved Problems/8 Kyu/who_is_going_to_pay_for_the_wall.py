# Question: Who is going to pay for the wall?
# Categories: 8 Kyu

def who_is_paying(name: str) -> list[str]:
    if len(name) <= 2:
        return [name]

    return [name, name[:2]]