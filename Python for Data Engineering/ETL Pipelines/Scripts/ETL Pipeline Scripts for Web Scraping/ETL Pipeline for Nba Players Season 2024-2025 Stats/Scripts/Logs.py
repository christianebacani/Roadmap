import Extract
import Transform
import Load
from datetime import datetime

# Logs

def logs(message):
    format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(format)
    
    logfile = 'logfile.txt'

    with open(logfile, 'a') as f:
        f.write(f'{timestamp} : {message}\n')


logs('[PROD] ETL Pipeline for Web Scraping Nba Stats Data of Season 2024-2025 Started')

# Extract
logs('[PROD] Extract Phase Started')
nbaStatsUrl = 'https://www.basketball-reference.com/leagues/NBA_2025'
teamStandingsHtml, teamRatingsHtml, coachesStatsHtml, playerStatsHtml = Extract.extract(nbaStatsUrl)
logs('[PROD] Extract Phase Ended')

# Transform
logs('[PROD] Transform Phase Started')
eastStandings, westStandings, teamRatings, coachStats, playerStats = Transform.transform(teamStandingsHtml, teamRatingsHtml, coachesStatsHtml, playerStatsHtml)
logs('[PROD] Transform Phase Ended')

# Load
logs('[PROD] Loasd Phase Started')
message = Load.load(eastStandings, westStandings, teamRatings, coachStats, playerStats)
print(message)
logs('[PROD] Loasd Phase Ended')


logs('[PROD] ETL Pipeline for Web Scraping Nba Stats Data of Season 2024-2025 Ended')