# Load

def load(transformedDailyWeatherDataFrom2024, dailyWeatherParameterData, dailyWeatherMetaData):
    dailyWeatherDataFrom2024TargetFilepath = 'Target Data Files\\Historical Weather Data from 2024 of Balanga City, Bataan\\daily_weather_data_from_2024.csv'
    dailyWeatherParameterDataTargetFilepath = 'Target Data Files\\Historical Weather Data from 2024 of Balanga City, Bataan\\daily_weather_parameter_data.csv'
    dailyWeatherMetaDataTargetFilepath = 'Target Data Files\\Historical Weather Data from 2024 of Balanga City, Bataan\\daily_weather_metadata.csv'

    transformedDailyWeatherDataFrom2024.to_csv(dailyWeatherDataFrom2024TargetFilepath, index=False)
    dailyWeatherParameterData.to_csv(dailyWeatherParameterDataTargetFilepath, index=False)
    dailyWeatherMetaData.to_csv(dailyWeatherMetaDataTargetFilepath, index=False)

    return transformedDailyWeatherDataFrom2024, dailyWeatherParameterData, dailyWeatherMetaData