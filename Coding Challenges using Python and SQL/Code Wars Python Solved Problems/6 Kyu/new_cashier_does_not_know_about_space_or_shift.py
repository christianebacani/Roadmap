# Question: New Cashier Does Not Know About Space or Shift
# Categories: 6 Kyu

def get_order(order: str) -> str:
    menus = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']
    result = []

    for i in range(len(menus)):
        for j in range(len(order)):
            substring = order[j : j + len(menus[i])]

            if len(substring) != len(menus[i]):
                continue

            if substring == menus[i]:
                result.append(substring.capitalize())
    
    return ' '.join(result)