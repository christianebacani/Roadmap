# 1667.) Fix Names in a Table
# Categories : Pandas

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    fixed_users = pd.DataFrame(columns=['user_id', 'name'])
    
    for _, row in users.iterrows():
        fixed_users = pd.concat([fixed_users, pd.DataFrame({'user_id' : [row.get('user_id')], 
                                                            'name' : [str(row.get('name')).capitalize()]})], ignore_index=True)

    fixed_users = fixed_users.sort_values(by=['user_id'])
    
    return fixed_users

        