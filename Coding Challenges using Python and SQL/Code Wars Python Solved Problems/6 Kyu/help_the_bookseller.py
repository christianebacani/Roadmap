# Question: Help the bookseller!
# Categories: 6 Kyu

def stock_list(stocklist: list[str], categories: list[str]) -> list[str]:
    if stocklist == []:
        return ''

    categories_and_quantity = {}

    for i in range(len(categories)):
        total_quantity = 0

        for j in range(len(stocklist)):
            if categories[i] == stocklist[j][0]:
                total_quantity += int(stocklist[j].split()[1])
        
        categories_and_quantity[categories[i]] = total_quantity
    
    result = []

    for category, quantity in categories_and_quantity.items():
        result.append('(' + category + ' : ' + str(quantity) + ')')
    
    return ' - '.join(result)