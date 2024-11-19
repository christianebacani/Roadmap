import pandas as pd
import glob
import xml.etree.ElementTree as ET

# Extraction Job

def extract():
    # Extract CSV File
    def extract_from_csv(csvfile):
        df = pd.read_csv(csvfile)
        return df 
    

    # Extract JSON File
    def extract_from_json(jsonfile):
        df = pd.read_json(jsonfile, lines=True)
        return df 
    

    # Extract XML File
    def extract_from_xml(xmlfile):
        df = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        
        for row in root:
            car_model = str(row.find('car_model').text)
            year_of_manufacture = int(row.find('year_of_manufacture').text)
            price = float(row.find('price').text)
            fuel = str(row.find('fuel').text)
            
            xml_df = pd.DataFrame({'car_model' : car_model, 'year_of_manufacture' : year_of_manufacture, 'price' : price, 'fuel' : fuel}, index=[0])

            df = pd.concat([df, xml_df], ignore_index=True)
    
        return df

    # Initialize Dataframe to store parsed data
    dataframe = pd.DataFrame(columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])

    # Filepath of source data
    sourcefilepath = 'Roadmap\\Python for Data Engineering\\ETL Pipelines\\Source Data Files\\Car Prices Datasets\\*'

    for file in glob.glob(sourcefilepath):
        if file[-4:] == '.csv':
            dataframe = pd.concat([dataframe, extract_from_csv(file)], ignore_index=True)
    
        elif file[-5:] == '.json':
            dataframe = pd.concat([dataframe, extract_from_json(file)], ignore_index=True)
        
        elif file[-4:] == '.xml':
            dataframe = pd.concat([dataframe, extract_from_xml(file)], ignore_index=True)
    
    return dataframe
