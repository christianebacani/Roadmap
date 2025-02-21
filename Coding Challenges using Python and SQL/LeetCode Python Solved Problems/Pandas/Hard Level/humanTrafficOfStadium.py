# 601.) Human Traffic of Stadium
# Categories : Pandas

import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['id', 'visit_date', 'people'])
    stadium_dict = {}

    for _, row in stadium.iterrows():
        id = int(row.get('id'))
        visit_date = row.get('visit_date')
        people = int(row.get('people'))
        
        stadium_dict[id] = {'visit_date' : visit_date, 'people' : people}
    
    for i in range(3, len(stadium) + 1):
        if (stadium_dict[i]['people'] >= 100) and (stadium_dict[i - 1]['people'] >= 100) and (stadium_dict[i - 2]['people'] >= 100):
            added_dataframe = pd.DataFrame({'id' : [i - 2, i - 1, i], 
                                            'visit_date' : [stadium_dict[i - 2]['visit_date'], stadium_dict[i - 1]['visit_date'], stadium_dict[i]['visit_date']],
                                            'people' : [stadium_dict[i - 2]['people'], stadium_dict[i - 1]['people'], stadium_dict[i]['people']]})
            
            output_df = pd.concat([output_df, added_dataframe], ignore_index=True)
    
    output_df.drop_duplicates(keep='first', inplace=True)
    output_df.sort_values(by=['visit_date'], ascending=[True])
    
    return output_df