# Question: Update inventory in your smartphone store
# Categories: 6 Kyu

def update_inventory(current_stock: list[tuple[int, str]], new_stock: list[tuple[int, str]]) -> list[tuple[int, str]]:
    result = []
    
    for i in range(len(current_stock)):
        current_quantity = current_stock[i][0]
        current_product = current_stock[i][1]

        for j in range(len(new_stock)):
            new_quantity = new_stock[j][0]
            new_product = new_stock[j][1]

            if current_product == new_product:
                result.append(tuple([current_quantity + new_quantity, new_product]))
                break
    
    updated_current_stock = []
    updated_new_stock = []

    for i in range(len(current_stock)):
        products = []

        for j in range(len(result)):
            products.append(result[j][1])
        
        if current_stock[i][1] not in products:
            updated_current_stock.append(current_stock[i])

    result.extend(updated_current_stock)
    
    for i in range(len(new_stock)):
        products = []

        for j in range(len(result)):
            products.append(result[j][1])
        
        if new_stock[i][1] not in products:
            updated_new_stock.append(new_stock[i])
    
    result.extend(updated_new_stock)
    products = []

    for i in range(len(result)):
        products.append(result[i][1])
    
    products.sort()
    sorted_result = []

    for i in range(len(products)):
        for j in range(len(result)):
            if products[i] == result[j][1]:
                sorted_result.append(result[j])
                break
    
    return sorted_result