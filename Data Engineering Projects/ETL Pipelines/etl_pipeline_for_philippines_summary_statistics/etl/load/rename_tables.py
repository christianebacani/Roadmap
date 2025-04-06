'''
    Rename table names
'''
def rename_tables(base_filename: str) -> str:
    '''
        Rename function to rename table names
    '''
    renamed_table_names = {
        'accommodation_and_food_service_activities_establishments': 'accomm_and_food_service_acts_est',
        'administrative_and_support_service_activities_establishments': 'administ_and_support_service_acts_est',
        'arts_entertainment_and_recreation_establishments': 'arts_entertain_and_recreation_est',
        'education_establishments': 'education_est',
        'financial_and_insurance_activities_establishments': 'financial_and_insurance_acts_est',
        'human_health_and_social_work_activities_establishments': 'human_health_and_soc_work_acts_est',
        'information_and_communication_establishments': 'info_and_comm_est',
        'other_service_activities_establishments': 'other_service_acts_est',
        'professional_scientific_and_technical_activities_establishments': 'prof_scientific_and_tech_acts_est',
        'real_estate_activities_establishments': 'real_estate_acts_est',
        'transportation_and_storage_establishments': 'transport_and_storage_est'
    }
    
    # Replacing base filename with a table name using hashmap to get the compact and shorter length of table name per base filename
    if base_filename in renamed_table_names:
        return renamed_table_names[base_filename]
    
    return base_filename
