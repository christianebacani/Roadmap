# Load

def load(playersData):
    targetFilepath = 'Target Data Files\\Nba Players Data for the Season 2024-2025\\players_data_season_2024.csv'
    playersData.to_csv(targetFilepath, index=False)
    
    return playersData

