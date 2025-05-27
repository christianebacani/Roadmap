# Question: My head is at the wrong end!
# Categories: 8 Kyu

def fix_the_meerkat(arr: list[str]) -> list[str]:
    head = arr[-1]
    body = arr[1]
    tail = arr[0]

    return [head, body, tail]