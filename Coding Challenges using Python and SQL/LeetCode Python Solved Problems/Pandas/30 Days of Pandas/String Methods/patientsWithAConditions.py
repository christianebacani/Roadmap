# 1527.) Patients With a Condition
# Categories : Pandas

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients_with_diabetes = pd.DataFrame(columns=['patient_id', 'patient_name', 'conditions'])
    
    for _, row in patients.iterrows():
        patient_id = row.get('patient_id')
        patient_name = row.get('patient_name')
        conditions_list = str(row.get('conditions')).split()

        for condition in conditions_list:
            if condition.startswith('DIAB1'):
                patients_with_diabetes = pd.concat([patients_with_diabetes, pd.DataFrame({'patient_id' : [patient_id],
                                                                                          'patient_name' : [patient_name],
                                                                                          'conditions' : [' '.join(conditions_list)]})], ignore_index=True)

    return patients_with_diabetes