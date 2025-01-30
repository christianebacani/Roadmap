# 2889.) Reshape Data: Pivot
# Category : Pandas

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivotDf = weather.pivot(index='month', columns='city', values='temperature')
    return pivotDf
    