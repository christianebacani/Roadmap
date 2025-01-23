import Validate
import pandas as pd

# Transform

def transform(teamStandingsHtml, teamRatingsHtml, coachStatsHtml, playerStatsHtml):
    eastStandings = teamStandingsHtml.find('div', {'id' : 'div_confs_standings_E'}).find('tbody')
    eastStandingRows = eastStandings.find_all('tr')

    eastStandingDict = {'team_name' : [], 'wins' : [], 'losses' : [], 'win_loss_pct' : [], 
                        'gb' : [], 'pts_per_g' : [], 'opp_pts_per_g' : [], 'srs' : []}


    westStandings = teamStandingsHtml.find('div', {'id' : 'div_confs_standings_W'}).find('tbody')
    westStandingRows = westStandings.find_all('tr')

    westStandingDict = {'team_name' : [], 'wins' : [], 'losses' : [], 'win_loss_pct' : [],
                        'gb' : [], 'pts_per_g' : [], 'opp_pts_per_g' : [], 'srs' : []}    


    for row in eastStandingRows: 
        eastStandingDict['team_name'].append(row.find('th', {'data-stat' : 'team_name'}).find('a').text)

        for attribute in list(eastStandingDict.keys()):
            if attribute != 'team_name':
                eastStandingDict[attribute].append(row.find('td', {'data-stat' : attribute}).text)
            

    for row in westStandingRows:
        westStandingDict['team_name'].append(row.find('th', {'data-stat' : 'team_name'}).find('a').text)

        for attribute in list(westStandingDict.keys()):
            if attribute != 'team_name':
                westStandingDict[attribute].append(row.find('td', {'data-stat' : attribute}).text)
    

    eastStandingDf = pd.DataFrame(eastStandingDict)
    westStandingDf = pd.DataFrame(westStandingDict)

    eastStandingDf, westStandingDf = Validate.cleanTeamStandingsData(eastStandingDf, westStandingDf)



    teamRatingsTable = teamRatingsHtml.find('tbody')
    teamRatingsRows = teamRatingsTable.find_all('tr')

    teamRatingsDict = {'ranker' : [], 'team_name' : [], 'conf_id' : [], 'div_id' : [],
                       'wins' : [], 'losses' : [], 'win_loss_pct' : [], 'mov' : [],
                       'off_rtg' : [], 'def_rtg' : [], 'net_rtg' : [], 'mov_adj' : [],
                       'off_rtg_adj' : [], 'def_rtg_adj' : [], 'net_rtg_adj' : []}
    

    for row in teamRatingsRows:
        teamRatingsDict['ranker'].append(row.find('th', {'data-stat' : 'ranker'}).text)
        
        for attribute in list(teamRatingsDict.keys()):
            if attribute != 'ranker':
                teamRatingsDict[attribute].append(row.find('td', {'data-stat' : attribute}).text)
    

    teamRatingsDf = pd.DataFrame(teamRatingsDict)

    teamRatingsDf = Validate.cleanTeamRatingsData(teamRatingsDf)



    coachStatsTable = coachStatsHtml.find('tbody')
    coachStatsRows = coachStatsTable.find_all('tr')
    
    coachStatsDict = {'coach' : [], 'team' : [], 'seas_num_franch' : [], 'seas_num_overall' : [],
                      'cur_g' : [], 'cur_w' : [], 'cur_l' : [], 'fr_g' : [], 'fr_w' : [],
                      'fr_l' : [], 'car_g' : [], 'car_w' : [], 'car_l' : [], 'car_wpct' : [],
                      'cur_g_p' : [], 'cur_w_p' : [], 'cur_l_p' : [], 'fr_g_p' : [], 
                      'fr_w_p' : [], 'fr_l_p' : [], 'car_g_p' : [], 'car_w_p' : [], 'car_l_p' : []}


    for row in coachStatsRows:
        coachStatsDict['coach'].append(row.find('th', {'data-stat' : 'coach'}).text)
        
        for attribute in list(coachStatsDict.keys()):
            if attribute != 'coach':
                coachStatsDict[attribute].append(row.find('td', {'data-stat' : attribute}).text)
    
    coachStatsDf = pd.DataFrame(coachStatsDict)

    coachStatsDf = Validate.cleanCoachStatsData(coachStatsDf)



    playerStatsTable = playerStatsHtml.find('tbody')
    playerStatsRows = playerStatsTable.find_all('tr')

    playerStatsDict = {'ranker' : [], 'name_display' : [], 'age' : [], 'team_name_abbr' : [], 'pos' : [],
                       'games' : [], 'games_started' : [], 'mp_per_g' : [], 'fg_per_g' : [], 'fga_per_g' : [],
                       'fg_pct' : [], 'fg3_per_g' : [], 'fg3a_per_g' : [], 'fg3_pct' : [], 'fg2_per_g' : [],
                       'fg2a_per_g' : [], 'fg2_pct' : [], 'efg_pct' : [], 'ft_per_g' : [], 'fta_per_g' : [],
                       'ft_pct' : [], 'orb_per_g' : [], 'drb_per_g' : [], 'trb_per_g' : [], 'ast_per_g' : [],
                       'stl_per_g' : [], 'blk_per_g' : [], 'tov_per_g' : [], 'pf_per_g' : [], 'pts_per_g' : []}
    

    for row in playerStatsRows:
        playerStatsDict['ranker'].append(row.find('th', {'data-stat' : 'ranker'}).text)

        for attribute in list(playerStatsDict.keys()):
            if attribute != 'ranker':
                playerStatsDict[attribute].append(row.find('td', {'data-stat' : attribute}).text)

    playerStatsDf = pd.DataFrame(playerStatsDict)

    playerStatsDf = Validate.cleanPlayerStatsData(playerStatsDf)


    return eastStandingDf, westStandingDf, teamRatingsDf, coachStatsDf, playerStatsDf 
