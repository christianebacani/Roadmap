# Question: Coding Meetup #4 - Higher-Order Functions Series - Find the first Python developer
# Categories: 7 Kyu

def get_first_python(users: list[dict[str, str]]) -> str:
    for i in range(len(users)):
        firstName = users[i]['first_name']
        country = users[i]['country']
        language = users[i]['language']

        if language == 'Python':
            return f'{firstName}, {country}'
    
    return 'There will be no Python developers'