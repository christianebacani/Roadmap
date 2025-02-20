# 3374.) First Letter Capitalization III
# Categories : Pandas

import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['content_id', 'original_text', 'converted_text'])

    for _, row in user_content.iterrows():
        content_id = row.get('content_id')
        content_text = row.get('content_text')

        content_text_lst = str(content_text).split()
        converted_text = []

        for word in content_text_lst:
            if '-' in word:
                word = word.split('-')
                word = [char.capitalize() for char in word]
                word = '-'.join(word)        
                converted_text.append(word)

            else:
                word = word.capitalize()
                converted_text.append(word)
        
        converted_text = ' '.join(converted_text)
        output_df = pd.concat([output_df, pd.DataFrame({'content_id' : content_id, 'original_text' : content_text, 'converted_text' : converted_text}, index=[0])], ignore_index=True)
    
    return output_df
