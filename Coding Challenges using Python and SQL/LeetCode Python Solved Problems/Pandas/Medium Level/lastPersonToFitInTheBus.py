# 1204.) Last Person to Fit in the Bus
# Categories : Pandas

import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue.sort_values(by=['turn'], ascending=[True], inplace=True)
    qualified_queue = pd.DataFrame(columns=['person_name', 'weight', 'turn'])
    total_weight = 0
    
    for _, row in queue.iterrows():
        person_name = row.get('person_name')
        weight = int(row.get('weight'))
        turn = int(row.get('turn'))
        
        total_weight += weight
        
        if total_weight <= 1000:
            qualified_queue = pd.concat([qualified_queue, pd.DataFrame({'person_name' : person_name, 'weight' : weight, 'turn' : turn}, index=[0])], ignore_index=True)
        
        else:
            break
    
    qualified_queue.sort_values(by=['turn'], ascending=[False], inplace=True)
    
    for index, person_name in enumerate(list(qualified_queue['person_name'])):
        index += 1

        if index == 1:
            return pd.DataFrame({'person_name' : person_name}, index=[0])
        