from datetime import datetime
import Extract
import Transform
import Load

# Logs

def logs(message):
    format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(format)
    
    logfile = 'logfile.txt'

    with open(logfile , 'a') as f:
        f.write(f'{message} : {timestamp}\n')

logs('(PROD) : ETL Pipeline using Nba API Started')

# Extract
logs('(PROD) : Extract Phase Started')
nbaPlayersData = Extract.extract()
print('All Nba Players Data of the Season 2024-2025 :\n')
print(nbaPlayersData)
logs('(PROD) : Extract Phase Ended')

# Transform
logs('(PROD) : Transform Phase Started')
transformedPlayersData = Transform.transform(nbaPlayersData)
print('\nAll Nba Players Data of the Season 2024-2025 :\n')
print(transformedPlayersData)
logs('(PROD) : Transform Phase Ended')

# Load
logs('(PROD) : Load Phase Started')
loadedPlayersData = Load.load(transformedPlayersData)
print('\nAll Nba Players Data of the Season 2024-2025 :\n')
print(loadedPlayersData)
logs('(PROD) : Load Phase Ended')

logs('(PROD) : ETL Pipeline using Nba API Ended')