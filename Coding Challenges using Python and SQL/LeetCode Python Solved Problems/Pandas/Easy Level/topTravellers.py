# 1407.) Top Travellers
# Categories : Pandas

import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['name', 'travelled_distance'])
    user_ids = list(users['id'])
    user_id_total_distance = {}
    
    for user_id in user_ids:
        total_distance = 0

        for _, row in rides.iterrows():
            rides_user_id = row.get('user_id')
            distance = row.get('distance')

            if user_id == rides_user_id:
                total_distance += distance

        user_id_total_distance[user_id] = total_distance

    for user_id, total_distance in user_id_total_distance.items():
        for _, row in users.iterrows():
            id = row.get('id')
            name = row.get('name')

            if user_id == id:
                output_df = pd.concat([output_df, pd.DataFrame({'name' : name, 'travelled_distance' : total_distance}, index=[0])])
    
    output_df.sort_values(by=['travelled_distance', 'name'], ascending=[False, True], inplace=True)

    return output_df
