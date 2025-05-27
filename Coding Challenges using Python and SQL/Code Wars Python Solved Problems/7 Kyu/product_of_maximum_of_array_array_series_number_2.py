# Question: Product Of Maximum Of Array (Array Series #2)
# Categories: 7 Kyu

def max_product(lst: list[int], n_largest_elements: int):
    lst = sorted(lst, reverse=True)
    chosen_elements = lst[:n_largest_elements]
    product = 1

    for i in range(len(chosen_elements)):
        product *= chosen_elements[i]
    
    return product