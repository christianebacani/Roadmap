import pandas as pd

# Transform

def transform(filmsData):
    filmsDict = {'film' : [], 'year' : [], 'rottenTomatoesTop100' : []}

    for row in filmsData:
        records = list(row.find_all('td'))

        for i in range(len(records)):
            if i == 1:
                filmsDict['film'].append(str(records[i].text).replace('\n', ''))
            
            elif i == 2:
                filmsDict['year'].append(str(records[i].text).replace('\n', ''))

            elif i == 3:
                filmsDict['rottenTomatoesTop100'].append(str(records[i].text).replace('\n', ''))
            
            pass

    filmsDf = pd.DataFrame(filmsDict)
    
    filmsDf.loc[filmsDf['year'] == 'unranked', 'year'] = '0'
    filmsDf.loc[filmsDf['rottenTomatoesTop100'] == 'unranked', 'rottenTomatoesTop100'] = '0'
 
    indices = []
    for index, row in filmsDf.iterrows():
        year = int(row.get('year'))
        if year < 2000:
            indices.append(index)
    
    filmsDf.drop(index=indices, inplace=True)
    filmsDf.reset_index(drop=True, inplace=True)

    filmsDf.drop(index=[25, 26, 27, 28, 29, 30], inplace=True)
    
    return filmsDf