'''
    Rename Module
'''
import pandas as pd

def rename_police_dept_inci_reports_2003_to_may_2018_dataset_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        police_dept_inci_reports_2003_to_may_2018
        dataset columns
    '''
    dataframe.rename(columns={
        'pdid': 'id',
        'incidntnum': 'incident_number',
        'dayofweek': 'day_of_the_week',
        'pddistrict': 'police_dept_district',
        'x': 'location_x_axis',
        'y': 'location_y_axis'
    }, inplace=True)
    
    unncessary_columns = [
        'location', ':@computed_region_6qbp_sg9q', 
        ':@computed_region_qgnn_b9vv', ':@computed_region_26cr_cadq', 
        ':@computed_region_ajp5_b2md', ':@computed_region_yftq_j783', 
        ':@computed_region_p5aj_wyqh', ':@computed_region_rxqg_mtj9', 
        ':@computed_region_bh8s_q3mv', ':@computed_region_fyvs_ahh9', 
        ':@computed_region_9dfj_4gjx', ':@computed_region_n4xg_c4py', 
        ':@computed_region_4isq_27mq', ':@computed_region_fcz8_est8', 
        ':@computed_region_pigm_ib2e', ':@computed_region_9jxd_iqea', 
        ':@computed_region_6pnf_4xz7', ':@computed_region_6ezc_tdp2', 
        ':@computed_region_h4ep_8xdi', ':@computed_region_nqbw_i6c3', 
        ':@computed_region_2dwj_jsy4', ':@computed_region_jwn9_ihcz'
    ]
    dataframe.drop(columns=unncessary_columns, inplace=True)

    return dataframe

def rename_police_dept_inci_reports_2018_to_present_dataset_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        police_dept_inci_reports_2018_to_present
        dataset columns
    '''
    dataframe.rename(columns={
        'cad_number': 'computer_aided_dispatch_number',
        'filed_online': 'is_filed_online',
        'cnn': 'centerline_node_network'
    }, inplace=True)

    dataframe.drop(columns=[
        'point', ':@computed_region_jwn9_ihcz', ':@computed_region_jg9y_a9du', ':@computed_region_h4ep_8xdi', 
        ':@computed_region_n4xg_c4py', ':@computed_region_nqbw_i6c3', ':@computed_region_viu7_rrfi', ':@computed_region_26cr_cadq', ':@computed_region_qgnn_b9vv'
    ], inplace=True)
    
    return dataframe

def rename_summary_of_inci_reports_dataset_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
        Rename function to rename
        summary_of_inci_reports
        dataset columns
    '''
    dataframe.rename(columns={
        'by_month_incident_date': 'per_month_incident_date',
        'point': 'geolocation_point'
    }, inplace=True)
    
    return dataframe