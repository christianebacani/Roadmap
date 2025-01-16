import pandas as pd
import glob

# Extract Job

def extract():
    def extract_from_json(jsonfile):
        json_data = pd.read_json(jsonfile)
        return json_data

    extracted_vct_df = pd.DataFrame(columns=['playerName', 'team', 'rating', 'region',
                                             'playerStatistics', 'agent', 'playerCategory'])
    
    source_filepath = 'Source Data Files\\Valorant Champions Tour 2024 Datasets\\*.json'
    
    for jsonfile in glob.glob(source_filepath):
        extracted_vct_df = pd.concat([extracted_vct_df, extract_from_json(jsonfile)], ignore_index=True)
    
    return extracted_vct_df