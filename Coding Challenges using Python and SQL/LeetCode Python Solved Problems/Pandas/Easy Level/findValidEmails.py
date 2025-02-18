# 3436.) Find Valid Emails
# Categories : Pandas

import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['user_id', 'email'])

    for _, row in users.iterrows():
        user_id = row.get('user_id')
        email = row.get('email')
        emailATCount = 0

        for char in email:
            if char == '@':
                emailATCount += 1

        try:
            email_lst = email.split('@')
            prefix_email = ''.join(email_lst[0])
            postfix_email = ''.join(email_lst[1]).replace('.com', '')
        
            if (emailATCount == 1) and (email[-4:] == '.com') and (prefix_email.isalnum()) and (postfix_email.isalpha()):
                output_df = pd.concat([output_df, pd.DataFrame({'user_id' : user_id, 'email' : email}, index=[0])], ignore_index=True)        

        except IndexError:
            continue
    
    output_df.sort_values(by=['user_id'], ascending=[True], inplace=True)

    return output_df
