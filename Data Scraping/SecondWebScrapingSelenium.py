from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import pandas as pd
import re 

# Function for customizing Web Driver
def web_driver():
    options = webdriver.EdgeOptions()

    options.add_argument('--verbose')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--blink-settings-imagesEnabled=false')

    service = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')

    driver = webdriver.Edge(service=service, options=options)
    
    return driver

# Call the function
driver = web_driver()
driver.get('https://quotes.toscrape.com/') # URL of the Website

# Execute script after scrolling from the top to bottom
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# Wait for the website to locate the elements
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="col-md-8"]'))
)

# Find the elements
containers = driver.find_elements(By.XPATH, '//div[@class="col-md-8"]')

# Store data
all_data = []

for container in containers:
    try:
        all_data.append(container.text) # Parse the elements into text and store it in the list

    except Exception as e:
        print(f"Error Code : {e}") 

# Ensure to close the Web Driver
driver.quit()

# Combined the data into a single string
text = '\n\n'.join(all_data)
sentences = text.split('\n') # Split to different rows

# Exclude specific rows that is irrelevant
df = pd.DataFrame(sentences).iloc[2:32].reset_index(drop=True)
print(df)

# Save into CSV File Format
df.to_csv('quotes_toscrape.csv', index=False)
print("Converted into CSV File Format!")

# Access the CSV Filepath
csv_filepath = 'D:\\Visual Studio Codes\\quotes_toscrape.csv'

df = pd.read_csv(csv_filepath)

# Specify the array to store the values
quotes = []
authors = []
keywords = []

# Loop to extract the specific strings
for i in range(0, len(df), 3):
    if i + 3 < len(df):
        quote = df.iloc[i, 0] # Extract the quote
        author = df.iloc[i+1, 0].split(' ')[1:3] # Extract the Author Name
        keyword_list = df.iloc[i+2, 0].split(': ')[1].split() # Extract the keywords
        
        keyword = [word.title() for word in keyword_list] # Store the keywords inside a list

        # Store the text inside the arrays
        quotes.append(quote)
        authors.append(' '.join(author))
        keywords.append(', '.join(keyword))

    else:
        break

# Specify the column name
formatted_df = pd.DataFrame({'Quote' : quotes, 
                            'Author' : authors, 
                            'Keyword' : keywords})

print(formatted_df)

# Save again into the CSV File Format!
# Overwriting the former file
formatted_df.to_csv('quotes_toscrape.csv', index=False)
print("Successfully Scrape!")

