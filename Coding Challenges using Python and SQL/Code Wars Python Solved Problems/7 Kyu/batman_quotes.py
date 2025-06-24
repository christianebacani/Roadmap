# Question: Batman Quotes
# Categories: 7 Kyu

class BatmanQuotes(object):

    @staticmethod
    def get_quote(quotes: list[str], hero: str) -> str:
        index_of_the_message = ''

        for i in range(len(hero)):
            if hero[i].isdigit():
                index_of_the_message += hero[i]
                break
        
        index_of_the_message = int(index_of_the_message)

        if hero[0] == 'J':
            hero = 'Joker'
        
        elif hero[0] == 'B':
            hero = 'Batman'
        
        else:
            hero = 'Robin'

        return f'{hero}: {quotes[index_of_the_message]}'