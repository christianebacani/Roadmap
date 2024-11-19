import pandas as pd

# Tranformation Job

def transform(df):
    columns = ['car_model', 'year_of_manufacture', 'price', 'fuel']
    
    # Cleaning records from the dataframe
    for col in columns:
        if col in ['car_model', 'fuel']:
            df[f'{col}'] = df[f'{col}'].fillna('No Name Specified')
        
        else:
            df[f'{col}'] = df[f'{col}'].fillna(0)


    dataframe = pd.DataFrame(columns=columns)


    # Transforming records from the dataframe
    for _, row in df.iterrows():
        car_model = str(row.get('car_model'))
        car_model = [char.capitalize() for char in car_model.split()]
        car_model = ' '.join(car_model) # Converted into capitalize string records

        year_of_manufacture = int(row.get('year_of_manufacture')) 
        price = round(float(row.get('price')), 2) # Round to 2 decimal places
        fuel = str(row.get('fuel').capitalize())
        
        transformed_df = pd.DataFrame({'car_model' : car_model, 'year_of_manufacture' : year_of_manufacture, 'price' : price, 'fuel' : fuel}, index=[0])

        dataframe = pd.concat([dataframe, transformed_df], ignore_index=True)


    return dataframe
