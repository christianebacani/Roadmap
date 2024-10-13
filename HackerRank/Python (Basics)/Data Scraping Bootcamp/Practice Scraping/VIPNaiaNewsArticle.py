# Import libraries/modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import pandas as pd
import re 
from keybert import KeyBERT

# Function for initializing the parameters and path of Web Driver
def web_driver():
    # Initialize the arguments for parameters
    options = webdriver.EdgeOptions()

    # Setting up the attributes of the parameters of the Web Driver
    options.add_argument('--verbose')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--blink-settings=imagesEnabled=false')

    # Initialize the Path
    service = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')

    # Define the path and the parameters
    options = webdriver.Edge(service=service, options=options)

    # Return the configured parameters and path of Web Driver (Edge)
    return options

# Execute the function
driver = web_driver()

# URL
driver.get('https://www.rappler.com/business/naia-vip-access-fee/?utm_source=Facebook&utm_campaign=SocialFlow&utm_medium=Social')

# Wait until the window page are fully loaded
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# Wait until the elements are located after loaded
WebDriverWait(driver, 35).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="article-main-section"]'))
)

# Get the specified div elements
containers = driver.find_elements(By.XPATH, '//div[@class="article-main-section"]') 

# Array to store the data
data = []

for element in containers:
    try:
        # Fetch the data from div element
        data.append(element.text) 

    # Catch error    
    except Exception as e:
        print(f"Error Code : {e}")


# Combined data
combined_data = '\n\n'.join(data)

# Split into rows
rows = combined_data.split('\n')

# Parse the rows into df
df = pd.DataFrame(rows, columns=['News Article'])

# Remove empty rows
df = df[df['News Article'].str.strip() != '']

# Include necessary rows only
df = df.iloc[:27].reset_index(drop=True)

# Save into CSV File
df.to_csv('D:\\Visual Studio Codes\\Data Scraping Bootcamp\\Practice Scraping\\NAIA Vip News Article.csv', index=False)
print("Successfully Saved into CSV!")


# TODO : Write more Python Scripts here...