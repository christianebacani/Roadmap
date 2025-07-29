# Question: For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre
# Categories: 8 Kyu

def quote(fighter: str) -> str:
    fighter = fighter.split()

    for i in range(len(fighter)):
        fighter[i] = fighter[i].capitalize()

    fighter = ' '.join(fighter)

    if fighter == 'George Saint Pierre':
        return 'I am not impressed by your performance.'

    return 'I\'d like to take this chance to apologize.. To absolutely NOBODY!'