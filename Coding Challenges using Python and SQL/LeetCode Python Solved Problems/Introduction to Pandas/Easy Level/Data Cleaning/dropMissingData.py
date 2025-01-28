# 2883.) Drop Missing Data
# Category : Pandas 

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    invalidIndices = []
    
    for index, row in students.iterrows():
        name = str(row.get('name'))

        if name in ['None', 'NaN', 'NAN', 'nan']:
            invalidIndices.append(index)
    
    students.drop(index=invalidIndices, inplace=True)

    return students