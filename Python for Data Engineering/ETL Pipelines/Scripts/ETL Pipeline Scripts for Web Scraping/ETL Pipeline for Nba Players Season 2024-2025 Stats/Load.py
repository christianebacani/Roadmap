from sqlalchemy import create_engine
import pandas as pd

# Load

def load(eastStandings, westStandings, teamRatings, coachStats, playerStats):
        username = '<YOUR_USERNAME>'
        password = '<YOUR PASSWORD>'
        hostname = '<HOSTNAME>'
        dbName = 'nba'

        engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{hostname}/{dbName}')
        csvFilepath = 'Target Data Files\\Nba Data\\CSV Files'
        

        eastStandingsFilepath = f'{csvFilepath}\\east_standings.csv'
        eastStandings.to_csv(eastStandingsFilepath, index=False)
        eastStandings.to_sql('east_standings', engine, if_exists='replace', index=False)
        
        westStandingsFilepath = f'{csvFilepath}\\west_standings.csv'
        westStandings.to_csv(westStandingsFilepath, index=False)
        westStandings.to_sql('west_standings', engine, if_exists='replace', index=False)

        teamRatingsFilepath = f'{csvFilepath}\\team_ratings.csv'
        teamRatings.to_csv(teamRatingsFilepath, index=False)
        teamRatings.to_sql('team_ratings', engine, if_exists='replace', index=False)

        coachStatsFilepath = f'{csvFilepath}\\coach_stats.csv'
        coachStats.to_csv(coachStatsFilepath, index=False)
        coachStats.to_sql('coach_stats', engine, if_exists='replace', index=False)

        playerStatsFilepath = f'{csvFilepath}\\player_stats.csv'
        playerStats.to_csv(playerStatsFilepath, index=False)
        playerStats.to_sql('player_stats', engine, if_exists='replace', index=False)


        return 'Successfully loaded all the data in the Local MySQL Database'