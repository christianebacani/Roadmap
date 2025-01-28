# 2877.) Create a DataFrame from List
# Category : Pandas

import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    studentDf = pd.DataFrame(student_data, columns=['student_id', 'age'])
    
    return studentDf
