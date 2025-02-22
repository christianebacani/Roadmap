# 608.) Tree Node
# Categories : Pandas

import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    output_df = pd.DataFrame(columns=['id', 'type'])
    tree[['p_id']] = tree[['p_id']].fillna(0)

    for _, row in tree.iterrows():
        id = row.get('id')
        p_id = row.get('p_id')
        
        if p_id == 0:
            output_df = pd.concat([output_df, pd.DataFrame({'id' : id, 'type' : 'Root'}, index=[0])], ignore_index=True)
        
        elif p_id in list(tree['id']) and id in list(tree['p_id']):
            output_df = pd.concat([output_df, pd.DataFrame({'id' : id, 'type' : 'Inner'}, index=[0])], ignore_index=True)

        elif p_id in list(tree['id']) and id not in list(tree['p_id']):
            output_df = pd.concat([output_df, pd.DataFrame({'id' : id, 'type' : 'Leaf'}, index=[0])], ignore_index=True)
    
    return output_df
