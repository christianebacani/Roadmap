import pandas as pd

# Transform Module

def transform(gadgetsDF):
    transformedGadgetsDict = {'Device Name' : [], 'Price' : [], 'Description' : [], 'Device Type' : [], 'Review Count' : []}

    for _, row in gadgetsDF.iterrows():
        deviceName = row.get('Device Name')
        
        if (deviceName[-3:] == '...'):
            deviceName = row.get('Description')
            deviceName = str(deviceName).split(', ')
            deviceName = deviceName[0]
            
            transformedGadgetsDict['Device Name'].append(deviceName)
            
        else:
            transformedGadgetsDict['Device Name'].append(deviceName)
            
        transformedGadgetsDict['Price'].append(f'${float(str(row.get('Price')).replace('$', '')):.1f}')
        transformedGadgetsDict['Description'].append(row.get('Description'))
        transformedGadgetsDict['Device Type'].append(row.get('Device Type'))
        transformedGadgetsDict['Review Count'].append(row.get('Review Count'))

    transformedGadgetsDF = pd.DataFrame(transformedGadgetsDict)
    
    return transformedGadgetsDF