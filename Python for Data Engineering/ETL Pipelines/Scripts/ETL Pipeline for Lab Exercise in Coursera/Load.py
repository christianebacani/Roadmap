import pandas as pd

# Loading Job

def load(df):
    # Load the Trasnformed Data into one consolidated format for further processing
    target_file = 'transformed_car_prices.csv'
    df.to_csv(target_file, index=False)

    dataframe = pd.read_csv(target_file)
    return dataframe