# Coding Meetup #11 - Higher-Order Functions Series - Find the average age
# Categories: 7 Kyu

def get_average(lst: list[dict[str, str]]) -> int: 
    ages = [lst[i]['age'] for i in range(len(lst))]
    return round(sum(ages) / len(ages))