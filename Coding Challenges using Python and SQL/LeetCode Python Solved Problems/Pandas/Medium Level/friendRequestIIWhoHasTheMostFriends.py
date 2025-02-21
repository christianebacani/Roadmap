# 602.) Friend Request II: Who Has the Most Friends
# Categories : Pandas

import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['id', 'num'])
    user_ids = []
    user_id_and_friends_count = {}
    
    for _, row in request_accepted.iterrows():
        user_ids.append(row.get('requester_id'))
        user_ids.append(row.get('accepter_id'))
    
    distinct_user_ids = list(set(user_ids))
    
    for distinct_user_id in distinct_user_ids:
        num = 0

        for requester_id in list(request_accepted['requester_id']):
            if distinct_user_id == requester_id:
                num += 1

        for accepter_id in list(request_accepted['accepter_id']):
            if distinct_user_id == accepter_id:
                num += 1

        user_id_and_friends_count[distinct_user_id] = num

    max_count = max(list(set(user_id_and_friends_count.values())), default=0)
    
    for user_id, friends_count in user_id_and_friends_count.items():
        if max_count == friends_count:
            output_df = pd.concat([output_df, pd.DataFrame({'id' : user_id, 'num' : friends_count}, index=[0])], ignore_index=True)
    
    return output_df

