# Question: Coding Meetup #14 - Higher-Order Functions Series - Order the food
# Categories: 7 Kyu

def order_food(lst: list[dict[str, str | int]]) -> dict[str, int]: 
    count_of_food_options = {}

    for i in range(len(lst)):
        if lst[i]['meal'] not in list(count_of_food_options.keys()):
            count_of_food_options[lst[i]['meal']] = 0
    
    for food, _ in count_of_food_options.items():
        count = 0

        for i in range(len(lst)):
            if food == lst[i]['meal']:
                count += 1
        
        count_of_food_options[food] = count
    
    return count_of_food_options