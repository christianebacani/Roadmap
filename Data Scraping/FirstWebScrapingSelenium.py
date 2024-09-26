from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import pandas as pd
import re 

def web_driver():
    options = webdriver.EdgeOptions()

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1200')

    service = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')

    driver = webdriver.Edge(service=service, options=options)
    return driver

driver = web_driver()
driver.get('https://www.scrapethissite.com/pages/simple/')

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="container"]'))
)

containers = driver.find_elements(By.XPATH, '//div[@class="container"]')

all_data = []

for container in containers:
    try:
        all_data.append(container.text)
    except Exception as e:
        print(f"Error Code : {e}")

strings = '\n\n'.join(all_data)
sentences = strings.split('\n')

df = pd.DataFrame(sentences)

df.to_csv('countries.csv', index=False)
print("Successfully Converted into CSV File Format!")
driver.close()

csv_filepath = 'D:\\Visual Studio Codes\\countries.csv'

df = pd.read_csv(csv_filepath, header=None).iloc[11:1010].reset_index(drop=True)



countries = []
capitals = []
populations = []
areas = []

try:
    for i in range(0, len(df), 4):
        if i + 3 < len(df):
            country = df.iloc[i,0]
            capital = df.iloc[i+1, 0].split(': ')[1]
            population = int(df.iloc[i+2, 0].split(': ')[1])
            area = float(df.iloc[i+3, 0].split(': ')[1])
                        


            countries.append(country)
            capitals.append(capital)
            populations.append(population)
            areas.append(area)

        else:
            break

except Exception as e:
    print(f"Error Code : {e}")

normalized_df = pd.DataFrame({'Country' : countries,
                              'Capital' : capitals,
                              'Population' : populations,
                              'Area' : areas})

print(normalized_df)

normalized_df.to_csv('country_normalized.csv', index=False)
print("Successfully Normalized!")









