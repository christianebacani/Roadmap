# Import Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import pandas as pd
import re 
from keybert import KeyBERT

# Web Driver Function
def web_driver():
    # Configuring the parameters of the Edge Web Driver
    options = webdriver.EdgeOptions()

    # Parameters of the Edge Web Driver
    options.add_argument('--verbose')
    options.add_argument('--disable-gpu')
    options.add_argument('--blink-settings-imagesEnabled=false')
    options.add_argument('--window-settings=1290,1200')
    options.add_argument('--disable-dev-shm-usage')

    # Defining the executable path of the Web Driver
    service = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')

    # Setting up the Web Driver Executable and the parameters
    driver = webdriver.Edge(service=service, options=options)

    # Return the configured and parameterized Web Driver (Edge) 
    return driver

# Execute the function
driver = web_driver()
# URL to Scrape
driver.get('https://www.codecademy.com/resources/blog/how-to-use-github-to-strengthen-your-resume/?utm_source=Facebook&utm_medium=organic-social&utm_content=fb_10_07_24_&_github_for_resume=')

# Function to wait for all the presence of all HTML Elements are located
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="entry-content"]'))
)

# Parse the specified HTML Elements
container = driver.find_elements(By.XPATH, '//div[@class="entry-content"]')

# Array to store store the fetched data from the parser
data = []

# Iterate through the parsed data
for element in container:
    try:
        # Fetch every element in the parsed data
        data.append(element.text)
    
    # Catch the error
    except Exception as e:
        print(f"Error Code : {e}")

# Close the Web Driver
driver.close()

# Combined the elements of the array
string = '\n'.join(data)

# Split into multiple rows
rows = string.split('\n')

# Parse the fetched data into a Dataframe
df = pd.DataFrame(rows, columns=['Content'])

# Remove empty rows
df = df[df['Content'].str.strip() != '']
print(df)

# Include necessary rows only
df = df.iloc[:75].reset_index(drop=True)


# Save to CSV File
df.to_csv('github_resume.csv', index=False)
print("Successfully Converted into CSV File!")

# Read CSV
df = pd.read_csv('github_resume.csv')

# Clean Data Function using Regex
def clean_content(text):
    # Substitute unnecessary newline, tablline or whitespaces into a single space
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    text = text.strip() # Remove white spaces and unnecessary quotations

    # Return the Cleaned Data
    return text

# Execute the function into a specific columnn
df['Content'] = df['Content'].apply(clean_content)
print(df)

# KeyBERT Model to Generate Keywords
model = KeyBERT('distilbert-base-nli-mean-tokens')

# Function to generate keywords
def generate_keywords(text):
    # List comprehension to generate keywords using KeyBERT Model
    keywords = [keyword for keyword, score in model.extract_keywords(text)]

    # List comprehension to capitalize every keywords generated
    keywords_capitalize = [words.upper() for words in keywords]

    # Return as a single string per element inside the list
    return ', '.join(keywords_capitalize)

# Execute the funtion
df['Category'] = df['Content'].apply(generate_keywords)

# Save into CSV File
df.to_csv('github_resume.csv', index=False)
print("Successully Loaded in CSV File")

# Convert the Format (CSV - Txt)
textfile = 'github_resume.csv'.replace('.csv', '.txt')

# Function to Modify the newly converted text file
with open(textfile, 'w', encoding='utf-8', newline='\n') as text:
    # Write the Header of the text file
    text.write(f"Row\tContent\t 'Category'\n")
    # Iterate through the columns
    for i, row in df.iterrows():
        content = row.get('Content', 'No Content')
        category = row.get('Category', 'No Category')

        text.write(f"{i + 1}. {content}\t Categories : '{category}'\n")

text.close()
print("Successfully Web Scraped!")

