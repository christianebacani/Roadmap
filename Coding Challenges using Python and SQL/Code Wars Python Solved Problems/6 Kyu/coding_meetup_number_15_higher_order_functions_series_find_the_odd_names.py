# Question: Coding Meetup #15 - Higher-Order Functions Series - Find the odd names
# Categories: 6 Kyu

def find_odd_names(lst: list[dict[str, str | int]]) -> list[dict[str, str | int]]: 
    result = []

    for i in range(len(lst)):
        firstName = lst[i]['firstName']
        sum_of_ascii_codes = 0

        for j in range(len(firstName)):
            sum_of_ascii_codes += ord(firstName[j])

        if sum_of_ascii_codes % 2 != 0:
            result.append(lst[i])
    
    return result