# Question: Alan Partridge III - London
# Categories: 7 Kyu

def alan(arr: list[str]) -> str:
    stops_alan_mention = {
        'Rejection': 0,
        'Disappointment': 0,
        'Backstabbing Central': 0,
        'Shattered Dreams Parkway': 0   
    }

    for i in range(len(arr)):
        if arr[i] not in stops_alan_mention:
            continue

        stops_alan_mention[arr[i]] = stops_alan_mention[arr[i]] + 1
    
    for _, frequency in stops_alan_mention.items():
        if frequency == 0:
            return 'No, seriously, run. You will miss it.'
        
    return 'Smell my cheese you mother!'