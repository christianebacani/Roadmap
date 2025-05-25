# Question: Find the Middle of the Product
# Categories: 7 Kyu

def find_middle(st: str | None | int | list[int]) -> int:
    if not isinstance(st, str):
        return -1
    
    digits = []

    for i in range(len(st)):
        if st[i].isnumeric():
            digits.append(int(st[i]))
    
    if digits == []:
        return -1
    
    product = 1

    for i in range(len(digits)):
        product *= digits[i]

    product = str(product)

    if len(product) % 2 == 0:
        first_middle_index = (len(product) // 2) - 1
        second_middle_index = len(product) // 2

        return int(product[first_middle_index] + product[second_middle_index])

    middle_index = len(product) // 2
    return int(product[middle_index])