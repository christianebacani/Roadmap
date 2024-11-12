import glob
import pandas as pd 
import xml.etree.ElementTree as ET 

# Extracting Job

def extract():
    def extract_from_csv(data):
        df = pd.read_csv(data)
        return df 

    def extract_from_json(data):
        df = pd.read_json(data)
        return df

    def extract_from_xml(data):
        xml_df = pd.DataFrame(columns=['name', 'height', 'weight'])
        tree = ET.parse(data)
        root = tree.getroot()

        for person in root:
            name = person.find('name').text
            height = float(person.find('height').text)
            weight = float(person.find('weight').text)
            
            xml_df = pd.concat([xml_df, pd.DataFrame([{'name' : name, 'height' : height, 'weight' : weight}])], ignore_index=True)

        return xml_df
    
    # Pre-defined dataframe
    dataframe = pd.DataFrame(columns=['name', 'height', 'weight'])

    # Using glob module for filepath pattern matching and extract data with different formats
    for file in glob.glob('D:\\Visual Studio Codes\\Data Engineering Projects in Python\\project\\*'):
        if file[-5:] == '.json':
            dataframe = pd.concat([dataframe, extract_from_json(file)], ignore_index=True)
    
        elif file[-4:] == '.csv':
            dataframe = pd.concat([dataframe, extract_from_csv(file)], ignore_index=True)
        
        elif file[-4:] == '.xml':
            dataframe = pd.concat([dataframe, extract_from_xml(file)], ignore_index=True)

    return dataframe

print(extract())
