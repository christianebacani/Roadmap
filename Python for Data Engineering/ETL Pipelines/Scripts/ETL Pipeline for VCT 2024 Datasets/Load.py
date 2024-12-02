# Load Job

def load(transformed_vct_df):
    target_filepath = 'Target Data Files\\Transformed Data for VCT 2024 Datasets\\transformed_vct_2024.csv'

    transformed_vct_df.to_csv(target_filepath, index=False)
    return transformed_vct_df