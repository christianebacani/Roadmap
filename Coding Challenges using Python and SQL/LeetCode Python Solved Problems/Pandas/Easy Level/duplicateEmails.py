# 182.) Duplicate Emails
# Categories : Pandas

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicate_emails_Df = pd.DataFrame(columns=['Email'])
    emails = []

    for _, row in person.iterrows():
        email = row.get('email')

        if email in emails:
            duplicate_emails_Df = pd.concat([duplicate_emails_Df, pd.DataFrame({'Email' : [email]})], ignore_index=True)
        
        else:
            emails.append(email)

    duplicate_emails_Df.drop_duplicates(subset='Email', keep='first', inplace=True)

    return duplicate_emails_Df