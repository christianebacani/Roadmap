import requests
from bs4 import BeautifulSoup

def extract(nbaStatsUrl):
    responsTeamStandings = requests.get(url=f'{nbaStatsUrl}_standings.html')
    teamStandingsSoup = BeautifulSoup(responsTeamStandings.text, 'html.parser')

    responseTeamRatings = requests.get(url=f'{nbaStatsUrl}_ratings.html#ratings')
    teamRatingsSoup = BeautifulSoup(responseTeamRatings.text, 'html.parser')

    responseCoachesStats = requests.get(url=f'{nbaStatsUrl}_coaches.html')
    coachesStatsSoup = BeautifulSoup(responseCoachesStats.text, 'html.parser')

    responsePlayersStats = requests.get(url=f'{nbaStatsUrl}_per_game.html')
    playersStatsSoup = BeautifulSoup(responsePlayersStats.text, 'html.parser')


    return teamStandingsSoup.find('div', {'id' : 'all_standings'}), teamRatingsSoup.find('div', {'id' : 'div_ratings'}), coachesStatsSoup.find('div', {'id' : 'div_NBA_coaches'}), playersStatsSoup.find('div', {'id' : 'div_per_game_stats'})

