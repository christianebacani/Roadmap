# 1890.) The Latest Login in 2020
# Categories: Database

import pandas as pd
from datetime import datetime

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    user_and_login_dates = {}

    for _, row in logins.iterrows():
        user_id = row.get('user_id')

        if user_id not in list(user_and_login_dates.keys()):
            user_and_login_dates[user_id] = []
    
    for _, row in logins.iterrows():
        user_id = row.get('user_id')
        time_stamp = row.get('time_stamp')

        if str(time_stamp)[:4] == '2020':
            user_and_login_dates[user_id].append(str(time_stamp))

    output = {
        'user_id': [],
        'last_stamp': []
    }

    for user_id, time_stamps in user_and_login_dates.items():
        if len(time_stamps) == 0:
            continue

        time_stamps = sorted(time_stamps, reverse=True)

        output['user_id'].append(user_id)
        output['last_stamp'].append(datetime.strptime(time_stamps[0], '%Y-%m-%d %H:%M:%S'))
    
    df = pd.DataFrame(output)

    return df