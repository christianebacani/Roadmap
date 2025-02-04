import pandas as pd

# Validate Data

def cleanTeamStandingsData(eastStandings, westStandings):
    # Handle missing values
    eastStandings.loc[eastStandings['gb'] == '—', 'gb'] = '0.0'
    westStandings.loc[westStandings['gb'] == '—', 'gb'] = '0.0'

    # List that consist of column with floating point values in the dataframe
    teamStandingsFloatColumns = ['gb', 'pts_per_g', 'opp_pts_per_g', 'srs']

    # Validating the dataframe
    for column in teamStandingsFloatColumns:
        for index, value in enumerate(eastStandings[column]):
            eastStandings.loc[index, column] = f'{float(value):.2f}'
        
        for index, value in enumerate(westStandings[column]):
            westStandings.loc[index, column] = f'{float(value):.2f}'
    
    # Rename columns
    eastStandings.rename(columns={'team_name' : 'teamName', 'win_loss_pct' : 'winLossPct', 
                                  'gb' : 'gamesBehind', 'pts_per_g' : 'ptsPerGame', 
                                  'opp_pts_per_g' : 'opponentPtsPerGame', 'srs' : 'simpleRatingSystem'}, inplace=True)
    
    westStandings.rename(columns={'team_name' : 'teamName', 'win_loss_pct' : 'winLossPct',
                                  'gb' : 'gamesBehind', 'pts_per_g' : 'ptsPerGame', 
                                  'opp_pts_per_g' : 'opponentPtsPerGame', 'srs' : 'simpleRatingSystem'}, inplace=True)

    return eastStandings, westStandings



def cleanTeamRatingsData(teamRatings):
    # Rename columns
    teamRatings.rename(columns={'ranker' : 'rank', 'team_name' : 'team', 'conf_id' : 'conferenceId',
                                'div_id' : 'divisionId', 'win_loss_pct' : 'winLossPct', 
                                'mov' : 'marginOfVictory', 'off_rtg' : 'offensiveRating', 
                                'def_rtg' : 'defensiveRating', 'net_rtg' : 'netRating',
                                'mov_adj' : 'adjustedMarginOfVictory', 'off_rtg_adj' : 'adjustedOffensiveRating',
                                'def_rtg_adj' : 'adjustedDefensiveRating', 'net_rtg_adj' : 'adjustedNetRating'}, inplace=True)
    
    return teamRatings



def cleanCoachStatsData(coachStats):
    # Intialize a dictionary to store validated dataframes
    coachStatsDict = {}

    for column in list(coachStats.keys()):
        coachStatsDict[column] = []
    
    # Handle missing values
    for _, row in coachStats.iterrows():
        for column in list(coachStats.keys()):
            value = row.get(column)
            
            if (column[-1] == 'p') and (value == ''):
                coachStatsDict[column].append(0)
            
            else:
                coachStatsDict[column].append(value)

    coachStatsDf = pd.DataFrame(coachStatsDict)

    # Rename columns
    coachStatsDf.rename(columns={'seas_num_franch' : 'totalSeasonsWithFranch', 'seas_num_overall' : 'totalSeasonsOverall',
                                 'cur_g' : 'currentSeasonTotalGames', 'cur_w' : 'currentSeasonTotalWins', 'cur_l' : 'currentSeasonTotalLosses',
                                 'fr_g' : 'currentFranchiseTotalGames', 'fr_w' : 'currentFranchiseTotalWins', 'fr_l' : 'currentFranchiseTotalLosses', 
                                 'car_g' : 'careerTotalGames', 'car_w' : 'careerTotalWins', 'car_l' : 'careerTotalLosses',  'car_wpct' : 'careerWinPct', 
                                 'cur_g_p' : 'currentSeasonTotalPlayoffGames', 'cur_w_p' : 'currentSeasonTotalPlayoffWins', 
                                 'cur_l_p' : 'currentSeasonTotalPlayoffLosses', 'fr_g_p' : 'franchiseTotalPlayoffGames', 'fr_w_p' : 'franchiseTotalPlayoffWins',
                                 'fr_l_p' : 'franchiseTotalPlayoffLosses', 'car_g_p' : 'careerTotalPlayoffGames', 'car_w_p' : 'careerTotalPlayoffWins',
                                 'car_l_p' : 'careerTotalPlayoffLosses'}, inplace=True)
    
    return coachStatsDf



def cleanPlayerStatsData(playerStats):
    # Initialize a dictionary to store validated dataframes
    playerStatsDict = {}
    
    for column in list(playerStats.keys()):
        playerStatsDict[column] = []
    

    # Remove duplicate records of name_display column
    playerStats.drop_duplicates(subset='name_display', keep='first', inplace=True, ignore_index=True)
    

    # Remove unnecessary row/s
    for index, value in enumerate(playerStats['name_display']):
        if value == 'League Average':
            playerStats.drop(index=index, inplace=True)
            playerStats.reset_index(drop=True)
            break


    # Storing filtered dataframes to the dictionary
    for _, row in playerStats.iterrows():
        for column in list(playerStats.keys()):
            playerStatsDict[column].append(row.get(column))

    playerStatsDf = pd.DataFrame(playerStatsDict)


    # List that consist of colums with int, percentage, and floating point values of a dataframe
    columnWithIntValues = ['games', 'games_started']
    
    columnWithPctValues = ['fg_pct', 'fg3_pct', 'fg2_pct', 'efg_pct', 'ft_pct']

    columnWithFloatValues = ['mp_per_g', 'fg_per_g', 'fga_per_g', 
                             'fg3_per_g', 'fg3a_per_g', 'fg2_per_g', 
                             'fg2a_per_g', 'ft_per_g','fta_per_g', 
                             'orb_per_g', 'drb_per_g', 'trb_per_g', 
                             'ast_per_g', 'stl_per_g', 'blk_per_g', 
                             'tov_per_g', 'pf_per_g', 'pts_per_g']

    # Dictionary that consist of player names with special characters
    playerNameWithSpecialChars = {'Nikola JokiÄ' : 'Nikola Jokić', 'Luka DonÄiÄ' : 'Luka Dončić', 
                                  'Nikola VuÄeviÄ' : 'Nikola Vučević', 'Alperen ÅengÃ¼n' : 'Alperen Şengün',
                                  'Kristaps PorziÅÄ£is' : 'Kristaps Porziņģis', 'Dennis SchrÃ¶der' : 'Dennis Schröder',  
                                  'Jonas ValanÄiÅ«nas' : 'Jonas Valančiūnas', 'Nikola JoviÄ' : 'Nikola Jović',
                                  'Bogdan BogdanoviÄ' : 'Bogdan Bogdanović', 'Jusuf NurkiÄ' : 'Jusuf Nurkić', 
                                  'Vasilije MiciÄ' : 'Vasilije Micić', 'Moussa DiabatÃ©' : 'Moussa Diabaté',
                                  'Lester QuiÃ±ones' : 'Lester Quiñones', 'Armel TraorÃ©' : 'Armel Traoré', 
                                  'Karlo MatkoviÄ' : 'Karlo Matković', 'Vlatko ÄanÄar' : 'Vlatko Čančar', 'Dario' : 'Dario Šarić'}


    # Clean and validate the dataframe
    for index, row in playerStatsDf.iterrows():
        for column in list(playerStatsDf.keys()):
            value = row.get(column)

            if (column in columnWithIntValues) and (value == ''):
                playerStatsDf.loc[index, column] = 0

            elif (column in columnWithPctValues) and (value == ''):
                playerStatsDf.loc[index, column] = .000

            elif (column in columnWithFloatValues) and (value == ''):
                playerStatsDf.loc[index, column] = '0.00'

            elif (column in columnWithFloatValues) and (value != ''):
                playerStatsDf.loc[index, column] = f'{float(value):.2f}'

            elif (value in playerNameWithSpecialChars):
                playerStatsDf.loc[index, 'name_display'] = playerNameWithSpecialChars[value]
            
            elif (value[:5] == 'Dario'):
                playerStatsDf.loc[index, 'name_display'] = playerNameWithSpecialChars[value[:5]]
        
    # Rename columns
    playerStatsDf.rename(columns={'ranker' : 'rank', 'name_display' : 'playerName', 'team_name_abbr' : 'teamCode', 'pos' : 'position', 
                                  'games' : 'totalGames', 'games_started' : 'totalGamesStarted', 'mp_per_g' : 'totalMinutesPerGame', 
                                  'fg_per_g' : 'fieldGoalsPerGame', 'fga_per_g' : 'fieldGoalAttemptsPerGame', 'fg_pct' : 'fieldGoalsPct', 
                                  'fg3_per_g' : 'threePtFieldGoalsPerGame', 'fg3a_per_g' : 'threePtFieldGoalAttemptsPerGame', 
                                  'fg3_pct' : 'threePtFieldGoalsPct', 'fg2_per_g' : 'twoPtFieldGoalsPerGame', 'fg2a_per_g' : 'twoPtFieldGoalAttemptsPerGame',
                                  'fg2_pct' : 'twoPtFieldGoalsPct', 'efg_pct' : 'effectiveFieldGoalsPct', 'ft_per_g' : 'freeThrowsPerGame', 
                                  'fta_per_g' : 'freeThrowAttemptsPerGame', 'ft_pct' : 'freeThrowPct', 'orb_per_g' : 'offensiveReboundsPerGame',
                                  'drb_per_g' : 'defensiveReboundsPerGame', 'trb_per_g' : 'totalReboundsPerGame', 'ast_per_g' : 'assistsPerGame',
                                  'stl_per_g' : 'stealsPerGame', 'blk_per_g' : 'blocksPerGame', 'tov_per_g' : 'turnoversPerGame', 
                                  'pf_per_g' : 'personalFoulsPerGame', 'pts_per_g' : 'pointsPerGame'}, inplace=True)

    return playerStatsDf