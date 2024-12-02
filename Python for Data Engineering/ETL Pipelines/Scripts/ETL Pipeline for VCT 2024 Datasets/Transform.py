import pandas as pd

# Transform Job

def transform(extracted_vct_df):
    transformed_vct_df = pd.DataFrame(columns=['playerName', 'team', 'rating', 'region',
                                               'average_combat_score', 'kill_deaths', 'kill_assists_survived_traded',
                                               'average_damage_per_round', 'kills_per_round', 'assists_per_round',
                                               'first_kills_per_round', 'first_deaths_per_round', 'headshot_percentage',
                                               'clutch_success_percentage', 'agent', 'playerCategory'])

    # Transforming/Cleaning the valuse inside the JSON Object
    for _, row in extracted_vct_df.iterrows():
        recordsDict = {}

        # Parsing and cleaning the values in the dataframe
        recordsDict['playerName'] = str(row.get('playerName')).strip()
        recordsDict['team'] = str(row.get('team')).strip()
        recordsDict['rating'] = str(row.get('rating')).strip()
        recordsDict['region'] = str(row.get('region')).strip()    
        playerStatistics = row.get('playerStatistics')

        # Flattening the Nested JSON Object inside playerStatistics values
        recordsDict['average_combat_score'] = str(playerStatistics.get('average_combat_score')).strip()
        recordsDict['kill_deaths'] = str(playerStatistics.get('kill_deaths')).strip()
        recordsDict['kill_assists_survived_traded'] = str(playerStatistics.get('kill_assists_survived_traded')).strip().replace('%', '.0 %')
        recordsDict['average_damage_per_round'] = str(playerStatistics.get('average_damage_per_round')).strip()
        recordsDict['kills_per_round'] = str(playerStatistics.get('kills_per_round')).strip()
        recordsDict['assists_per_round'] = str(playerStatistics.get('assists_per_round')).strip()
        recordsDict['first_kills_per_round'] = str(playerStatistics.get('first_kills_per_round')).strip()
        recordsDict['first_deaths_per_round'] = str(playerStatistics.get('first_deaths_per_round')).strip()
        recordsDict['headshot_percentage'] = str(playerStatistics.get('headshot_percentage')).strip()
        recordsDict['clutch_success_percentage'] = str(playerStatistics.get('clutch_success_percentage')).strip()
        recordsDict['agent'] = row.get('agent')
        recordsDict['playerCategory'] = str(row.get('playerCategory')).strip()

        # Check for missing values and clean the data with a missing values
        for column, record in recordsDict.items():
            if (not record) and (column in ['playerName', 'team', 'region', 'agent', 'playerCategory']):
                recordsDict[column] = 'Not Specified'
    
            elif (not record) and (column in ['kill_assists_survived_traded', 'headshot_percentage', 'clutch_success_percentage']):
                recordsDict[column] = '0.0 %'

            elif (not record):
                recordsDict[column] = '0.0'

            # Formatting the agent values
            elif (record) and (column == 'agent'):
                agent = [word.capitalize() for word in record]
                agent = ', '.join(agent)
                recordsDict['agent'] = agent
            
            # Formatting the playerCategory values
            elif (record) and (column == 'playerCategory'):
                playerCategory = []
                for word in record.split('-'):
                    if word == 'vct':
                        playerCategory.append(word.upper())
                    else:
                        playerCategory.append(word.capitalize())
                recordsDict['playerCategory'] = '-'.join(playerCategory)                       

            else:
                pass
      
        parsed_df = pd.DataFrame({'playerName' : [recordsDict['playerName']],
                                  'team' : [recordsDict['team']],
                                  'rating' : [recordsDict['rating']],
                                  'region' : [recordsDict['region']],
                                  'average_combat_score' : [recordsDict['average_combat_score']],
                                  'kill_deaths' : [recordsDict['kill_deaths']],
                                  'kill_assists_survived_traded' : [recordsDict['kill_assists_survived_traded']],
                                  'average_damage_per_round' : [recordsDict['average_damage_per_round']],
                                  'kills_per_round' : [recordsDict['kills_per_round']],
                                  'assists_per_round' : [recordsDict['assists_per_round']],
                                  'first_kills_per_round' : [recordsDict['first_kills_per_round']],
                                  'first_deaths_per_round' : [recordsDict['first_deaths_per_round']],
                                  'headshot_percentage' : [recordsDict['headshot_percentage']],
                                  'clutch_success_percentage' : [recordsDict['clutch_success_percentage']],
                                  'agent' : [recordsDict['agent']],
                                  'playerCategory' : [recordsDict['playerCategory']]
                                  })

        transformed_vct_df = pd.concat([transformed_vct_df, parsed_df], ignore_index=True)

    return transformed_vct_df