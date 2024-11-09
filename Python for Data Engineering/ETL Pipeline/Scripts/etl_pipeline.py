import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import re 
import os


# ETL Pipeline

# Extract Data
def extract():
    def web_driver():
        options = webdriver.EdgeOptions()
        
        # Parameters of the Web Driver
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-settings=1920,1200')

        driver = webdriver.Edge(options=options)

        return driver
    
    # Execute the inner function
    driver = web_driver()
    
    # URL to scrape
    driver.get('https://hackernoon.com/a-guide-to-romantic-relationships-for-dummies-tech-people')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    
    container = driver.find_elements(By.XPATH, '//div[@class="sc-2e79ac2f-0 ktrYOp"]')

    data = []

    for elements in container:
        try:
            data.append(elements.text)
        except Exception as e:
            print(f"Error Code : {e}")
    
    # Format to string
    combinedData = '\n'.join(data)
    rows = combinedData.split('\n')
    
    df = pd.DataFrame(rows, columns=['Content']) # Initializing a Dataframe
    return df


# Transform Data
def transform(data):
    # Clean Data
    def clean_content(text):
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\n+', ' ', text)
        text = re.sub(r'\t+', ' ', text)
        text = text.strip()
        return text
    
    data = data[data['Content'] != ''] # Remove empty rows
    data['Content'] = data['Content'].apply(clean_content)

    return data # Return transformed dataframe


# Load Data
def load(data):
    # Loading the data into the Target Data Files Directory
    data.to_csv('D:\\Visual Studio Codes\\Data Engineering Projects in Python\\ETL Pipeline\\Target Data Files\\a_guide_for_romantic_relationship_tech_people.csv', index=False)
    
    csv_filepath = 'D:\\Visual Studio Codes\\Data Engineering Projects in Python\\ETL Pipeline\\Target Data Files\\a_guide_for_romantic_relationship_tech_people.csv'
    df = pd.read_csv(csv_filepath)

    textfile = csv_filepath.replace('.csv', '.txt')

    subHeaders = ['1. Never assume, Ask.', '2. ‘Listen’ to what your users do, not what they say.',
                  '3. Communicate clearly, always.', '4. Never forget delighters.',
                  '5. Keep iterating.']
    
    # Converting to Text File
    with open(textfile, 'w', encoding='utf-8', newline='\n') as f:
        f.write(f"\t\t\t\t\t\t\t\t'A Guide to Romantic Relationships for ̶d̶u̶m̶m̶i̶e̶s̶ Tech People'\n\n")

        for _, row in df.iterrows():
            content = row.get('Content', 'Content')

            # Write the subheaders by enclosing to single quotes
            if content in subHeaders:
                f.write(f"\n'{content}'\n\n")

            else:
                f.write(f"{content}\n")

    f.close()
    os.remove(csv_filepath) # Remove unused csv file data


# Logs Function
def logs(message):
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    with open('D:\\Visual Studio Codes\\Data Engineering Projects in Python\\ETL Pipeline\\Log Files\\logfile.txt', 'a') as f:
        f.write(f"{timestamp} : {message}\n")



# Executing the pipeline
logs('Extracting Data Job Started')
extracted_data = extract()
logs('Extracting Data Job Ended')

logs('Transforming Data Job Started')
transformed_data = transform(extracted_data)
logs('Transforming Data Job Ended')

logs('Loading Data Job Started')
load(transformed_data)
logs('Loading Data Job Ended')

