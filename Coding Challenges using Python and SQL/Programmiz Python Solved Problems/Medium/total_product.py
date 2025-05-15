# Question: Write a function to calculate the product of all items in a list
# Categories: Medium

def product_of_list(numbers : list[int]) -> int:
    total_product = 1

    for i in range(len(numbers)):
        total_product *= numbers[i]
    
    return total_product