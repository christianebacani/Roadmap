import pandas as pd

# Transform

def transform(extractedDailyWeatherDataFrom2024):
    # Dictionary to store daily weather metadata
    dailyWeatherParameterDataDict = {'time' : [], 'weather_code' : [], 'temperature_2m_max' : [], 'temperature_2m_min' : [], 'temperature_2m_mean' : [], 
                                      'apparent_temperature_max' : [], 'apparent_temperature_min' : [], 'apparent_temperature_mean' : [], 'sunrise' : [], 'sunset' : [], 
                                      'daylight_duration' : [], 'sunshine_duration' : [], 'precipitation_sum' : [], 'rain_sum' : [], 'snowfall_sum' : [], 
                                      'precipitation_hours' : [], 'wind_speed_10m_max' : [], 'wind_gusts_10m_max' : [], 'wind_direction_10m_dominant' : [], 'shortwave_radiation_sum' : [], 'et0_fao_evapotranspiration' : []}
    
    # Daily unit columns
    dailyUnitColumns = []

    for column in list(dailyWeatherParameterDataDict.keys()):
        dailyUnitColumns.append(column)

    # Dictionary to store daily weather data
    transformedDailyWeatherDataFrom2024Dict = {'time' : [], 'weather_code' : [], 'temperature_2m_max' : [], 'temperature_2m_min' : [], 'temperature_2m_mean' : [], 
                                               'apparent_temperature_max' : [], 'apparent_temperature_min' : [], 'apparent_temperature_mean' : [], 'sunrise' : [], 'sunset' : [],
                                               'daylight_duration' : [], 'sunshine_duration' : [], 'precipitation_sum' : [], 'rain_sum' : [], 'snowfall_sum' : [],
                                               'precipitation_hours' : [], 'wind_speed_10m_max' : [], 'wind_gusts_10m_max' : [], 'wind_direction_10m_dominant' : [], 'shortwave_radiation_sum' : [],
                                               'et0_fao_evapotranspiration' : []}

    # Daily weather data columns
    dailyWeatherDataColumns = []

    for column in list(transformedDailyWeatherDataFrom2024Dict.keys()):
        dailyWeatherDataColumns.append(column)


    # Separating into separated dataframe, cleaning, and transforming parameter data from the JSON formatted daily weather data from 2024
    dailyUnitDict = extractedDailyWeatherDataFrom2024.get('daily_units')
    
    for dailyUnitColumn in dailyUnitColumns:
        dailyWeatherParameterDataDict[dailyUnitColumn].append(str(dailyUnitDict.get(dailyUnitColumn)).strip())
    

    # Separating into separated dataframe, cleaning, and transforming data from JSON formatted daily weather data from 2024
    dailyWeatherDataDict = extractedDailyWeatherDataFrom2024.get('daily')

    for dailyWeatherDataColumn in dailyWeatherDataColumns:
        dailyWeatherDataInnerRecordList = dailyWeatherDataDict.get(dailyWeatherDataColumn)
        
        if dailyWeatherDataColumn in ['time', 'sunrise', 'sunset']:
            for innerRecord in dailyWeatherDataInnerRecordList:
                transformedDailyWeatherDataFrom2024Dict[dailyWeatherDataColumn].append(str(innerRecord).strip())
            
        elif dailyWeatherDataColumn in ['weather_code', 'snowfall_sum', 'precipitation_hours', 'wind_direction_10m_dominant']:
            for innerRecord in dailyWeatherDataInnerRecordList:
                transformedDailyWeatherDataFrom2024Dict[dailyWeatherDataColumn].append(str(innerRecord).strip())

        elif dailyWeatherDataColumn in ['temperature_2m_max', 'temperature_2m_min', 'temperature_2m_mean', 'apparent_temperature_max', 'apparent_temperature_min', 'apparent_temperature_mean', 'daylight_duration', 'sunshine_duration', 'precipitation_sum', 'rain_sum', 'wind_speed_10m_max', 'wind_gusts_10m_max', 'shortwave_radiation_sum', 'et0_fao_evapotranspiration']:
            for innerRecord in dailyWeatherDataInnerRecordList:
                transformedDailyWeatherDataFrom2024Dict[dailyWeatherDataColumn].append(f'{float(str(innerRecord).strip()):.2f}')
    
        else:
            pass
    
    
    # Converting dictionary to dataframe
    dailyWeatherParameterData = pd.DataFrame(dailyWeatherParameterDataDict)
    transformedDailyWeatherDataFrom2024 = pd.DataFrame(transformedDailyWeatherDataFrom2024Dict)
    

    # Renaming columns from the dataframe
    dailyWeatherParameterData.rename(columns={'time' : 'time_unit', 'weather_code' : 'weather_code_unit',
                                                'temperature_2m_max' : 'temperature_2m_max_unit', 'temperature_2m_min' : 'temperature_2m_min_unit',
                                                'temperature_2m_mean' : 'temperature_2m_mean_unit', 'sunrise' : 'sunrise_unit', 
                                                'sunset' : 'sunset_unit', 'daylight_duration' : 'daylight_duration_unit',
                                                'sunshine_duration' : 'sunshine_duration_unit', 'precipitation_sum' : 'precipitation_sum_unit',
                                                'rain_sum' : 'rain_sum_unit', 'snowfall_sum' : 'snowfall_sum_unit',
                                                'precipitation_hours' : 'precipitation_hours_unit', 'wind_speed_10m_max' : 'wind_speed_10m_max_unit',
                                                'wind_gusts_10m_max' : 'wind_gusts_10m_max_unit', 'wind_direction_10m_dominant' : 'wind_direction_10m_dominant_unit',
                                                'shortwave_radiation_sum' : 'shortwave_radiation_sum_unit', 'et0_fao_evapotranspiration' : 'et0_fao_evapotranspiration_unit'}, inplace=True)
    
    transformedDailyWeatherDataFrom2024.rename(columns={'time' : 'date', 'sunrise' : 'sunrise_time', 'sunset' : 'sunset_time'}, inplace=True)


    # Initialize a daily weather metadata dictionary
    dailyWeatherMetaDataDict = {'column_name' : [], 'data_type' : [], 'unit' : [], 'description' : []}

    metaDataDescriptionDict = {'date' : 'Date of the recorded daily weather data', 'weather_code' : 'The most severe weather condition on a given day',
                               'temperature_2m_max' : 'Maximum daily air temperature at 2 meters above ground',
                               'temperature_2m_min' : 'Minimum daily air temperature at 2 meters above ground',
                               'temperature_2m_mean' : 'Mean daily air temperature at 2 meters above ground',
                               'apparent_temperature_2m_max' : 'Maximum daily apparent temperature',
                               'apparent_temperature_2m_min' : 'Minimum daily apparent temperature',
                               'apparent_temperature_2m_mean' : 'Mean daily apparent temperature',
                               'sunrise_time' : 'Sunrise time', 'sunset_time' : 'Sunset time',
                               'daylight_duration' : 'Number of seconds of daylight per day', 
                               'sunshine_duration' : 'Number of seconds of sunshine per day', 
                               'precipitation_sum' : 'Sum of daily precipitation (including rain, showers and snowfall)',
                               'rain_sum' : 'Sum of daily rain', 'snowfall_sum' : 'Sum of daily snowfall',
                               'precipitation_hours' : 'The number of hours with rain', 'wind_speed_10m_max' : 'Maximum wind speed on a day',
                               'wind_gusts_10m_max' : 'Maximum wind gusts on a day', 
                               'wind_direction_10m_dominant' : 'Dominant wind direction', 'shortwave_radiation_sum' : 'The sum of solar radiaion on a given day in Megajoules',
                               'et0_fao_evapotranspiration' : 'Daily sum of ET₀ Reference Evapotranspiration of a well watered grass field'}
    
    # Storing column_name, data_type, unit, and description values in the metadata dictionary
    for column in list(transformedDailyWeatherDataFrom2024.keys()):
        dailyWeatherMetaDataDict['column_name'].append(column)
        
        if column in ['date', 'sunrise_time', 'sunset_time']:
            dailyWeatherMetaDataDict['data_type'].append('String')
        
        elif column in ['weather_code', 'snowfall_sum', 'precipitation_hours', 'wind_direction_10m_dominant']:
            dailyWeatherMetaDataDict['data_type'].append('Integer')
        
        else:
            dailyWeatherMetaDataDict['data_type'].append('Decimal')
    
    for column, unit in dailyUnitDict.items():
        dailyWeatherMetaDataDict['unit'].append(str(unit).strip())
    
    for column, description in metaDataDescriptionDict.items():
        dailyWeatherMetaDataDict['description'].append(description)
    
    # Convert metadata dictionary to dataframe
    dailyWeatherMetaData = pd.DataFrame(dailyWeatherMetaDataDict)


    return transformedDailyWeatherDataFrom2024, dailyWeatherParameterData, dailyWeatherMetaData
