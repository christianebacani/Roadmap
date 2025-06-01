# Question: Player Contact Manager
# Categories: 7 Kyu

def player_manager(players_information: str | None) -> list[dict[str, str | int]]:
    if players_information == '' or players_information is None:
        return []

    players_information = players_information.split(', ')
    player_information_formatted = []

    for i in range(0, len(players_information), 2):
        player_info = players_information[i : i + 2]
        player_name = player_info[0]
        player_contact = player_info[1]

        player_information_formatted.append([player_name, player_contact])
    
    players_information = player_information_formatted
    result = []

    for i in range(len(players_information)):
        result.append({
            'player': players_information[i][0],
            'contact': int(players_information[i][1])
        })
    
    return result