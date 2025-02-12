# 595.) Big Countries
# Category : Pandas

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    bigCountriesDf = pd.DataFrame(columns=['name', 'population', 'area'])
    
    for _, row in world.iterrows():
        area = int(row.get('area'))
        population = int(row.get('population'))

        if area >= 3000000 or population >= 25000000:
            bigCountriesDf = pd.concat([bigCountriesDf, pd.DataFrame({'name' : [row.get('name')],
                                                                      'population' : [population],
                                                                      'area' : [area]})], ignore_index=True)

    return bigCountriesDf
