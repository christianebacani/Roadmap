# Question: Maximum Product
# Categories: 7 Kyu

def adjacent_element_product(array: list[int]) -> int:
    products = []

    for i in range(1, len(array)):
        products.append(array[i - 1] * array[i])
    
    return max(products)