# 2891.) Method Chaining
# Category : Pandas

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filterDict = {'name' : [], 'weight' : []}

    for _, row in animals.iterrows():
        name = row.get('name')
        weight = int(row.get('weight'))

        if weight > 100:
            filterDict['name'].append(name)
            filterDict['weight'].append(weight)

    filterDf = pd.DataFrame(filterDict)


    sortedWeights = []

    for weight in filterDf['weight']:
        sortedWeights.append(weight)
    
    sortedWeights.sort(reverse=True)


    sortedDict = {'name' : []}

    for weight in sortedWeights:
        for _, row in filterDf.iterrows():
            animalWeight = row.get('weight')

            if weight == animalWeight:
                sortedDict['name'].append(row.get('name'))       
    
    sortedDf = pd.DataFrame(sortedDict)

    return sortedDf