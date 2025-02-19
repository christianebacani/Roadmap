# 180.) Consecutive Numbers
# Categories : Pandas

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['ConsecutiveNums'])
    numbers = list(logs['num'])

    for i in range(2, len(numbers)):
        if (numbers[i] == numbers[i - 1]) and (numbers[i] == numbers[i - 2]):
            output_df = pd.concat([output_df, pd.DataFrame({'ConsecutiveNums' : numbers[i]}, index=[0])], ignore_index=True)
    
    output_df.drop_duplicates(keep='first', inplace=True)
    return output_df