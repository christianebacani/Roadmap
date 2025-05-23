# Question: Coding Meetup #1 - Higher-Order Functions Series - Count the number of JavaScript developers coming from Europe
# Categories: 7 Kyu

def count_developers(lst: list[dict[str, str]]) -> int:
    number_of_javascript_devs_from_eu = 0

    for i in range(len(lst)):
        if lst[i]['continent'] == 'Europe' and lst[i]['language'] == 'JavaScript':
            number_of_javascript_devs_from_eu += 1
    
    return number_of_javascript_devs_from_eu