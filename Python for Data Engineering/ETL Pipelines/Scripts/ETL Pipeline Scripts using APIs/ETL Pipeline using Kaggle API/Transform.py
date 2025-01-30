import pandas as pd

# Transform

def transform(df):
    # Initialize a dictionary to store formatted data from the dataframe
    transformedEarthquakeData = {}

    for column in list(df.keys()):
        transformedEarthquakeData[column] = []
    
    

    decimalColumnNames = ['Depth', 'dmin', 'rms', 'horizontalError', 'depthError', 'magError']
    integerColumnNames = ['nst', 'gap', 'magNst']
    
    # Formatting inconsistent format from the dataframe and map to a new dataframe
    for column in list(df.keys()):
        for value in df[column]:
            if (column == 'Time') or (column == 'Updated'):
                value = str(value).replace('T', ' ').replace('Z', '')
            
            elif (column == 'Latitude') or (column == 'Longitude'):
                value = f'{float(str(value)):.4f}'

            elif (column in decimalColumnNames):
                value = f'{float(str(value)):.2f}'
            
            elif column == 'Mag':
                value = f'{float(str(value)):.1f}'

            elif (column in integerColumnNames):
                value = f'{float(str(value)):.0f}'
            
            elif column in ['MagType', 'Type', 'status']:
                value = str(value).capitalize()
            
            elif column in ['net', 'locationSource', 'magSource']:
                value = str(value).upper()
            
            transformedEarthquakeData[column].append(value)
    
    transformedEarthquakeDf = pd.DataFrame(transformedEarthquakeData)



    primaryColumnNames = ['Time', 'Place', 'Latitude', 'Longitude', 'ID', 'Mag']
    nullValues = ['NaN', 'NAN', 'nan']
    invalidIndices = []

    # Remove rows with missing values of primary columns
    for column in list(transformedEarthquakeDf.keys()):
        for index, value in enumerate(transformedEarthquakeDf[column]):
            if (column in primaryColumnNames) and (value in nullValues):
                invalidIndices.append(index)

    transformedEarthquakeDf.drop(index=invalidIndices, inplace=True)
    


    decimalValues, integerValues = [], []

    # Get the most occured non-NaN values (mode) per column in the dataframe
    for column in list(transformedEarthquakeDf.keys()):
        for value in transformedEarthquakeDf[column]:
            value = str(value)

            if (column in decimalColumnNames) and (value not in nullValues):
                decimalValues.append(f'{float(value):.2f}')
            
            elif (column in integerColumnNames) and (value not in nullValues):
                integerValues.append(value)
        
    decimalModeValue = f'{float(pd.Series(decimalValues).mode().iloc[0]):.2f}'
    integerModeValue = f'{float(pd.Series(integerValues).mode().iloc[0]):.0f}'
    

    
    # Initialize a dictionary to store cleaned data from the transformed dataframe
    cleanedEarthquakeDataDict = {}
    
    for column in list(transformedEarthquakeDf.keys()):
        cleanedEarthquakeDataDict[column] = []
    

    
    # Mapping cleaned data (replaced missing quantitative values with mode value) to a new dataframe
    for _, row in transformedEarthquakeDf.iterrows():
        for column in list(transformedEarthquakeDf.keys()):
            value = str(row.get(column))

            if (column in decimalColumnNames) and (value in nullValues):
                value = decimalModeValue
            
            elif (column in integerColumnNames) and (value in nullValues):
                value = integerModeValue
            
            cleanedEarthquakeDataDict[column].append(value)
            
    cleanedEarthquakeDf = pd.DataFrame(cleanedEarthquakeDataDict)
    

    # Remove unnecessary column
    cleanedEarthquakeDf.drop(columns=['Unnamed: 14'], inplace=True)

    # Rename columns
    cleanedEarthquakeDf.rename(columns={'Time' : 'time', 'Place' : 'place',  'Latitude' : 'latitude',
                                        'Longitude' : 'longitude', 'Depth' : 'depth',  'Mag' : 'magnitude',
                                        'MagType' : 'magnitudeType', 'nst' : 'totalNumberOfSeismicStations',
                                        'dmin' : 'minimumDistance',  'rms' : 'rootMeanSquare', 'net' : 'networkOfSeismographicStations',
                                        'ID' : 'id', 'Updated' : 'updatedTime', 'Type' : 'type', 'magError' : 'magnitudeError',
                                        'magNst' : 'totalNumberOfMagnitudeSeismicStations', 'magSource' : 'magnitudeSource'}, inplace=True)
    

    return cleanedEarthquakeDf