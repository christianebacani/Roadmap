# 3475.) DNA Pattern Recognition
# Categories: Database

import pandas as pd
import re

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    result_dict = {
        'sample_id': [],
        'dna_sequence': [],
        'species': [],
        'has_start': [],
        'has_stop': [],
        'has_atat': [],
        'has_ggg': []
    }

    for _, row in samples.iterrows():
        result_dict['sample_id'].append(int(row.get('sample_id')))
        result_dict['dna_sequence'].append(str(row.get('dna_sequence')))
        result_dict['species'].append(str(row.get('species')))
        
        dna_sequence = str(row.get('dna_sequence'))


        if re.search(r'^(ATG).*$', dna_sequence):
            result_dict['has_start'].append(1)
        
        else:
            result_dict['has_start'].append(0)


        if re.search(r'^.*(TAA)$', dna_sequence) or re.search(r'^.*(TAG)$', dna_sequence) or re.search(r'^.*(TGA)$', dna_sequence):
            result_dict['has_stop'].append(1)

        else:
            result_dict['has_stop'].append(0)


        if re.search(r'^.*(ATAT).*$', dna_sequence):
            result_dict['has_atat'].append(1)
        
        else:
            result_dict['has_atat'].append(0)
        
        
        if re.search(r'^.*(GGG).*$', dna_sequence):
            result_dict['has_ggg'].append(1)
        
        else:
            result_dict['has_ggg'].append(0)
    
    result = pd.DataFrame(result_dict)

    return result