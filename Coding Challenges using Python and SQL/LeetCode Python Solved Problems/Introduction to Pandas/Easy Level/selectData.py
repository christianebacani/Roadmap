# 2880. Select Data
# Category : Pandas

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    filteredDict = {'name' : [], 'age' : []}

    for _, row in students.iterrows():
        studentId = row.get('student_id', None)
        name = row.get('name', None)
        age = row.get('age', None)
        
        if studentId == 101:
            filteredDict['name'].append(name)
            filteredDict['age'].append(age)

    filteredDf = pd.DataFrame(filteredDict)
    
    return filteredDf