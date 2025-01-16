import pandas as pd

# Transform

def transform(nbaPlayersData):
    playersDataDict = {}
    for key in list(nbaPlayersData[0].keys()):
        if key not in ['id', 'playerId']:
            playersDataDict[key] = []

    for playerData in nbaPlayersData:
        for key in list(playersDataDict.keys()):
            data = playerData.get(key, None)

            if isinstance(data, str):
                playersDataDict[key].append(data)
            
            elif isinstance(data, (int, float)) and (key != 'season'):
                playersDataDict[key].append(f'{float(data):.2f}')
            
            elif key == 'season':
                playersDataDict['season'].append(data)
            
            elif (data == None) and (key in ['playerName', 'position', 'team']):
                playersDataDict[key].append('Not Specified')
            
            elif data == None:
                playersDataDict[key].append(0.00)
            
            pass
    
    playersData = pd.DataFrame(playersDataDict)
    playersData.rename(columns={'games' : 'totalGamesPlayed', 'gamesStarted' : 'totalGamesStarted', 'minutesPg' : 'totalMinutesPlayed',
                                'team' : 'teamCode'}, inplace=True)

    for index, seasonRecord in enumerate(playersData['season']):
        if seasonRecord == 2025:
            playersData.loc[index, 'season'] = '2024-2025'
    

    return playersData
