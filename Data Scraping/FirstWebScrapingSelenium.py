# Import Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import pandas as pd
import re 

# Function for customizable Web Driver
def web_driver():
    options = webdriver.EdgeOptions()

    options.add_argument('--no-sandbox') # No Sandbox, remove if you are using Docker Containers
    options.add_argument('--disable-gpu') # Disable GPU
    options.add_argument('--window-size=1920,1200') # Window Size for the Web Driver

    # Define the path for the Web Edge Driver
    service = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')

    # Web Driver
    driver = webdriver.Edge(service=service, options=options)
    return driver

# Call the function
driver = web_driver()
driver.get('https://www.scrapethissite.com/pages/simple/') # URL to Scrape

# Parameters before executing the script
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# Wait until the elements are located
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="container"]'))
)

# Get the elements inside the Website
containers = driver.find_elements(By.XPATH, '//div[@class="container"]')

all_data = []

# Scrape the elements inside the website
for container in containers:
    try:
        all_data.append(container.text)
    except Exception as e:
        print(f"Error Code : {e}")

# Combined into a single string
strings = '\n\n'.join(all_data)
sentences = strings.split('\n') # Split into multiple rows

# Define the Dataframe based on the rows
df = pd.DataFrame(sentences)

# Save as a CSV File
df.to_csv('countries.csv', index=False)
print("Successfully Converted into CSV File Format!")
driver.close() # Close the Driver

# Filepath of the CSV
csv_filepath = 'D:\\Visual Studio Codes\\countries.csv'

# Extract only the necessary rows
df = pd.read_csv(csv_filepath, header=None).iloc[11:1010].reset_index(drop=True)

# Column names
countries = []
capitals = []
populations = []
areas = []

# Get the values per rows and store it in a list
try:
    for i in range(0, len(df), 4):
        # Make sure the index is not out of range
        if i + 3 < len(df):
            country = df.iloc[i,0]
            capital = df.iloc[i+1, 0].split(': ')[1]
            population = int(df.iloc[i+2, 0].split(': ')[1])
            area = float(df.iloc[i+3, 0].split(': ')[1])
                        

            # Store in a list
            countries.append(country)
            capitals.append(capital)
            populations.append(population)
            areas.append(area)

        else:
            break

# Error Handler
except Exception as e:
    print(f"Error Code : {e}")

# Define the Dataframe based on the list
normalized_df = pd.DataFrame({'Country' : countries,
                              'Capital' : capitals,
                              'Population' : populations,
                              'Area' : areas})

print(normalized_df)

# Save and Overwrite the existing CSV File Format
normalized_df.to_csv('country_normalized.csv', index=False)
print("Successfully Normalized!")
