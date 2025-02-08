# 2886.) Change Data Type
# Category : Pandas

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    convertedDataTypeStudents = {'student_id' : [], 'name' : [],
                                 'age' : [], 'grade' : []}
    
    for _, row in students.iterrows():
        for column in list(students.keys()):
            if column in ['student_id', 'age', 'grade']:
                value = int(row.get(column))
            
            else:
                value = str(row.get(column))
            
            convertedDataTypeStudents[column].append(value)
    
    studentsDf = pd.DataFrame(convertedDataTypeStudents)
    
    return studentsDf