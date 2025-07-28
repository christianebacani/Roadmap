# Question: Removing Elements
# Categories: 8 Kyu

def remove_every_other(my_list: list[str]) -> list[str]:
    return [my_list[i] for i in range(len(my_list)) if i % 2 == 0]