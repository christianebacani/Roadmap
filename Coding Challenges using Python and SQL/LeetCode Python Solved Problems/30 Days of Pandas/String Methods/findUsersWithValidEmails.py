# 1517.) Find Users With Valid E-Mails
# Categories : Pandas

import pandas as pd
import re

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_emails = pd.DataFrame(columns=['user_id', 'name', 'mail'])

    for _, row in users.iterrows():
        user_id = row.get('user_id')
        name = row.get('name')
        mail = row.get('mail')

        try:
            lst = mail.split('@')
            prefix_name = lst[0]
            domain_name = f'@{lst[1]}'

        except IndexError:
            continue

        if (re.search(r'[A-Za-z]+', prefix_name[:1]) and not re.search(r'[~`!@#\$%\^\&\*\(\)\+=\[\]\{\}\|:;\'\"<,>\?/]+', prefix_name)) and (domain_name == '@leetcode.com'):
            valid_emails = pd.concat([valid_emails, pd.DataFrame({'user_id' : [user_id], 'name' : [name], 'mail' : [mail]})], ignore_index=True)
    
    return valid_emails
            