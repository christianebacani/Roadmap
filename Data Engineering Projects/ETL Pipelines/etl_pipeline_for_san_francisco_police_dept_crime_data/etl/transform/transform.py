'''
    Transform Module
'''
import pandas as pd
from datetime import datetime
from transform.rename import rename_police_dept_inci_reports_2003_to_may_2018_dataset_columns
from transform.rename import rename_police_dept_inci_reports_2018_to_present_dataset_columns
from transform.rename import rename_summary_of_inci_reports_dataset_columns

def transform_police_dept_inci_reports_2003_to_may_2018_datasets(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        police_dept_inci_reports_2003_to_may_2018
        datasets from stage datasets directory path
    '''
    renamed_dataframe = rename_police_dept_inci_reports_2003_to_may_2018_dataset_columns(dataframe)

    transformed_data = {}

    for column_name in list(renamed_dataframe.keys()):
        transformed_data[column_name] = []

    for _, row in renamed_dataframe.iterrows():
        transformed_data['id'].append(int(row.get('id')))
        transformed_data['incident_number'].append(int(row.get('incident_number')))
        transformed_data['incident_code'].append(int(row.get('incident_code')))
        
        category = str(row.get('category'))
        category_word_delimiters = ['/', '-', ' ']

        for i in range(len(category_word_delimiters)):
            if category_word_delimiters[i] in category:
                category = category.split(category_word_delimiters[i])
                category = [word.capitalize() for word in category]
                category = category_word_delimiters[i].join(category)
        
        category = category.split()
        category = [word.capitalize() for word in category]
        category = ''.join(category)
        transformed_data['category'].append(category)
    
        descript = str(row.get('descript')).split()
        descript = [word.capitalize() for word in descript]
        descript = ' '.join(descript)
        transformed_data['descript'].append(descript)
    
        transformed_data['day_of_the_week'].append(str(row.get('day_of_the_week')).capitalize())
        transformed_data['date'].append(datetime.strptime(str(row.get('date')).replace('T00:00:00.000', ''), '%Y-%m-%d'))    
        transformed_data['time'].append(str(row.get('time')))
        transformed_data['police_dept_district'].append(str(row.get('police_dept_district')).capitalize())
        
        resolution = str(row.get('resolution')).split()
        resolution = [word.capitalize() for word in resolution]
        transformed_data['resolution'].append(' '.join(resolution))

        address = str(row.get('address')).replace(' / ', ', ').split()
        formatted_address_name = []

        for i in range(len(address)):
            if address[i] == 'ST':
                formatted_address_name.append('St')
            
            elif address[i] == 'ST,':
                formatted_address_name.append('St,')

            elif address[i] == 'AV':
                formatted_address_name.append('Avenue')
            
            else:
                formatted_address_name.append(address[i].capitalize())
        
        transformed_data['address'].append(' '.join(formatted_address_name))

        transformed_data['location_x_axis'].append(float(row.get('location_x_axis')))
        transformed_data['location_y_axis'].append(float(row.get('location_y_axis')))

    transformed_dataframe = pd.DataFrame(transformed_data)

    return transformed_dataframe

def transform_police_dept_inci_reports_2018_to_present_datasets(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        police_dept_inci_reports_2018_to_present
        datasets from stage datasets directory path    
    '''
    renamed_dataframe = rename_police_dept_inci_reports_2018_to_present_dataset_columns(dataframe)
    
    transformed_data = {}
    for column in list(renamed_dataframe.keys()):
        transformed_data[column] = []
    
    column_and_imputed_data_values = {
        'computer_aided_dispatch_number': [],
        'intersection': [],
        'centerline_node_network': [],
        'analysis_neighborhood': [],
        'supervisor_district': [],
        'supervisor_district_2012': [],
        'latitude': [],
        'longitude': []
    }

    for computer_aided_dispatch_number in renamed_dataframe['computer_aided_dispatch_number']:
        if str(computer_aided_dispatch_number).lower() != 'nan':
            column_and_imputed_data_values['computer_aided_dispatch_number'].append(int(computer_aided_dispatch_number))
    
    for intersection in renamed_dataframe['intersection']:
        if str(intersection).lower() != 'nan':
            column_and_imputed_data_values['intersection'].append(str(intersection))

    for centerline_node_network in renamed_dataframe['centerline_node_network']:
        if str(centerline_node_network).lower() != 'nan':
            column_and_imputed_data_values['centerline_node_network'].append(int(centerline_node_network))
    
    for analysis_neighborhood in renamed_dataframe['analysis_neighborhood']:
        if str(analysis_neighborhood).lower() != 'nan':
            column_and_imputed_data_values['analysis_neighborhood'].append(str(analysis_neighborhood))

    for supervisor_district in renamed_dataframe['supervisor_district']:
        if str(supervisor_district).lower() != 'nan':
            column_and_imputed_data_values['supervisor_district'].append(int(supervisor_district))
    
    for supervisor_district_2012 in renamed_dataframe['supervisor_district_2012']:
        if str(supervisor_district_2012).lower() != 'nan':
            column_and_imputed_data_values['supervisor_district_2012'].append(int(supervisor_district_2012))
    
    for latitude in renamed_dataframe['latitude']:
        if str(latitude).lower() != 'nan':
            column_and_imputed_data_values['latitude'].append(float(latitude))
    
    for longitude in renamed_dataframe['longitude']:
        if str(longitude).lower() != 'nan':
            column_and_imputed_data_values['longitude'].append(float(longitude))
    
    for column, values in column_and_imputed_data_values.items():
        if isinstance(values[0], int):
            column_and_imputed_data_values[column] = int(pd.Series(values).median())
        
        elif isinstance(values[0], float):
            column_and_imputed_data_values[column] = float(pd.Series(values).mean())
        
        elif isinstance(values[0], str):
            column_and_imputed_data_values[column] = pd.Series(values).mode()[0]
        
    
    for _, row in renamed_dataframe.iterrows():
        transformed_data['incident_datetime'].append(datetime.strptime(str(row.get('incident_datetime')), '%Y-%m-%dT%H:%M:%S.%f'))
        transformed_data['incident_date'].append(datetime.strptime(str(row.get('incident_date')).split('T')[0], '%Y-%m-%d').date())
        transformed_data['incident_time'].append(datetime.strptime(str(row.get('incident_time')), '%H:%M').time())
        transformed_data['incident_year'].append(datetime.strptime(str(row.get('incident_year')), '%Y').year)
        transformed_data['incident_day_of_week'].append(str(row.get('incident_day_of_week')))
        transformed_data['report_datetime'].append(datetime.strptime(str(row.get('report_datetime')), '%Y-%m-%dT%H:%M:%S.%f'))
        transformed_data['row_id'].append(int(row.get('row_id')))
        transformed_data['incident_id'].append(int(row.get('incident_id')))
        transformed_data['incident_number'].append(int(row.get('incident_number')))
        transformed_data['computer_aided_dispatch_number'].append(int(float(str(row.get('computer_aided_dispatch_number')).lower().replace('nan', str(column_and_imputed_data_values['computer_aided_dispatch_number'])))))
        transformed_data['report_type_code'].append(str(row.get('report_type_code')))
        transformed_data['report_type_description'].append(str(row.get('report_type_description')))
        transformed_data['is_filed_online'].append(bool(str(row.get('is_filed_online')).lower().replace('nan', str(False))))
        transformed_data['incident_code'].append(int(row.get('incident_code')))
        transformed_data['incident_category'].append(str(row.get('incident_category')))
        transformed_data['incident_subcategory'].append(str(row.get('incident_subcategory')))
        transformed_data['incident_description'].append(str(row.get('incident_description')))
        transformed_data['resolution'].append(str(row.get('resolution')))

        intersection = str(row.get('intersection')).lower().replace('nan', column_and_imputed_data_values['intersection']).replace('\\', ', ').split()

        for i in range(len(intersection)):
            if intersection[i] == 'AVE':
                intersection[i] = 'Avenue'

            elif intersection[i] == 'AVE,':
                intersection[i] = 'Avenue,'
            
            elif intersection[i] == 'BLVD':
                intersection[i] = 'Boulevard'
            
            elif intersection[i] == 'BLVD,':
                intersection[i] = 'Bouelevard,'
            
            else:
                intersection[i] = intersection[i].strip().capitalize()
        
        transformed_data['intersection'].append(' '.join(intersection))
        transformed_data['centerline_node_network'].append(int(float(str(row.get('centerline_node_network')).lower().replace('nan', str(column_and_imputed_data_values['centerline_node_network'])))))
        transformed_data['police_district'].append(str(row.get('police_district')))
        transformed_data['analysis_neighborhood'].append(str(row.get('analysis_neighborhood')).lower().replace('nan', column_and_imputed_data_values['analysis_neighborhood']).capitalize())
        transformed_data['supervisor_district'].append(int(float(str(row.get('supervisor_district')).lower().replace('nan', str(column_and_imputed_data_values['supervisor_district'])))))
        transformed_data['supervisor_district_2012'].append(int(float(str(row.get('supervisor_district_2012')).lower().replace('nan', str(column_and_imputed_data_values['supervisor_district_2012'])))))
        transformed_data['latitude'].append(float(str(row.get('latitude')).lower().replace('nan', str(column_and_imputed_data_values['latitude']))))
        transformed_data['longitude'].append(float(str(row.get('longitude')).lower().replace('nan', str(column_and_imputed_data_values['longitude']))))
        
    transformed_dataframe = pd.DataFrame(transformed_data)

    return transformed_dataframe

def transform_summary_of_inci_reports_datasets(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Transform function to transform
        summary_of_inci_reports datasets 
        from stage datasets directory path    
    '''
    renamed_dataframe = rename_summary_of_inci_reports_dataset_columns(dataframe)

    transformed_data = {}
    
    for column in list(renamed_dataframe.keys()):
        if column != 'geolocation_point':
            transformed_data[column] = []

    transformed_data['geolocation_x_axis'] = []
    transformed_data['geolocation_y_axis'] = []

    geolocation_point_values = []

    for geolocation_point in renamed_dataframe['geolocation_point']:
        if str(geolocation_point).lower() != 'nan':
            geolocation_point_values.append(str(geolocation_point))

    geolocation_point_mode = pd.Series(geolocation_point_values).mode()[0]


    for _, row in renamed_dataframe.iterrows():
        transformed_data['per_month_incident_date'].append(datetime.strptime(str(row.get('per_month_incident_date')).split('T')[0], '%Y-%m-%d').date())
        transformed_data['incident_category'].append(str(row.get('incident_category')))
        transformed_data['analysis_neighborhood'].append(str(row.get('analysis_neighborhood')))
        transformed_data['count'].append(int(row.get('count')))
        
        geolocation_point = str(row.get('geolocation_point')).lower().replace('nan', geolocation_point_mode)
        geolocation_point = geolocation_point.lower()
        geolocation_point_unnecessary_values = ['point', '(', ')']

        for i in range(len(geolocation_point_unnecessary_values)):
            geolocation_point = geolocation_point.replace(geolocation_point_unnecessary_values[i], ' ')
        
        geolocation_point = geolocation_point.split()
        transformed_data['geolocation_x_axis'].append(float(geolocation_point[0].strip()))
        transformed_data['geolocation_y_axis'].append(float(geolocation_point[1].strip()))
    
    transformed_dataframe = pd.DataFrame(transformed_data)

    return transformed_dataframe