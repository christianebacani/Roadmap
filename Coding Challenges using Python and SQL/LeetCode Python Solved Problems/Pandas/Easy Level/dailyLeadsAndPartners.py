# 1693.) Daily Leads and Partners
# Categories : Pandas

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['date_id', 'make_name', 'unique_leads', 'unique_partners'])
    date_id_and_make_names = []

    for _, row in daily_sales.iterrows():
        date_id = row.get('date_id')
        make_name = row.get('make_name')

        date_id_and_make_names.append(tuple([date_id, make_name]))

    date_id_and_make_names = list(set(date_id_and_make_names))

    for date_id_and_make_name in date_id_and_make_names:
        date_id = date_id_and_make_name[0]
        make_name = date_id_and_make_name[1]

        lead_ids, partnet_ids = [], []
        unique_leads_count, unique_partners_count = 0, 0

        for _, inner_row in daily_sales.iterrows():
            inner_row_date_id = inner_row.get('date_id')
            inner_row_make_name = inner_row.get('make_name')
            inner_row_lead_id = inner_row.get('lead_id')
            inner_row_partner_id = inner_row.get('partner_id')

            if (date_id == inner_row_date_id and make_name == inner_row_make_name) and (inner_row_lead_id not in lead_ids):
                lead_ids.append(inner_row_lead_id)
                unique_leads_count += 1
            
            if (date_id == inner_row_date_id and make_name == inner_row_make_name) and (inner_row_partner_id not in partnet_ids):
                partnet_ids.append(inner_row_partner_id)
                unique_partners_count += 1
        
        output_df = pd.concat([output_df, pd.DataFrame({'date_id' : date_id, 'make_name' : make_name, 'unique_leads' : unique_leads_count, 'unique_partners' : unique_partners_count}, index=[0])], ignore_index=True)

    return output_df
            