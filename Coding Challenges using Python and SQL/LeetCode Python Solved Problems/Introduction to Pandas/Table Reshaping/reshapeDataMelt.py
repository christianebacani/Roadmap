# 2890.) Reshape Data : Melt
# Categories : Pandas

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    unpivotedDf = pd.melt(report, id_vars=['product'], value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], var_name='quarter', value_name='sales')   

    return unpivotedDf
