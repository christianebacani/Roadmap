# Question: Converting Currency II
# Categories: 7 Kyu

def solution(currency: str, list_of_money: list[float]) -> list[str]:
    currency_conversion = {
        'USD': [f'{num * 1.1363636:.2f}' for num in list_of_money],
        'EUR': [f'{num / 1.1363636:.2f}' for num in list_of_money]
    }
    list_of_money = currency_conversion[currency]
    
    for i in range(len(list_of_money)):
        money = list_of_money[i].split('.')[0][::-1]
        cents = list_of_money[i].split('.')[1]
        formattted_money = ''

        for index, digit in enumerate(money):
            index += 1

            if index == len(money):
                formattted_money += digit
                continue
            
            formattted_money += digit

            if index % 3 == 0:
                formattted_money += ','
        
        money = formattted_money[::-1] + '.' + cents
        list_of_money[i] = money
    
    for i in range(len(list_of_money)):
        if currency == 'USD':
            list_of_money[i] = '$' + list_of_money[i]
        
        else:
            list_of_money[i] = list_of_money[i] + '€'
    
    return list_of_money