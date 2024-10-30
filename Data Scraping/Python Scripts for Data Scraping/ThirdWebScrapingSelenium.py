# Import Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import pandas as pd
import re 
import os

# Function to initialize the parameters
def web_driver():
    # Initialize the Web Driver (Edge)
    options = webdriver.EdgeOptions()

    # Parameters
    options.add_argument('--verbose')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--blink-settings-imagesEnabled=false')
    
    # Define the Web Driver Path
    service = Service(executable_path='D:\\Edge WebDriver Folder\\msedgedriver.exe')

    # Define the path and the parameters
    options = webdriver.Edge(service=service, options=options)

    # Return the configured web driver
    return options

# Execute the function
driver = web_driver()

# Go to URL using the configured Web Driver
driver.get('https://dev.to/sheraz4194/good-commit-vs-bad-commit-best-practices-for-git-1plc?ref=dailydev')

# Wait until the documents are fully loaded in the web page
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')


# Wait until the specific div elements are located
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//div[@class="crayons-article__main"]'))
)

container = driver.find_elements(By.XPATH, '//div[@class="crayons-article__main"]')

data = []

for element in container:
    try:
        data.append(element.text)
    except Exception as e:
        print(f"Error Code : {e}")

# Format data for parsing into DF
combined_data = '\n'.join(data) 
splitted_data = combined_data.split('\n')

df = pd.DataFrame(splitted_data, columns=['Good Vs. Bad Commit Article'])
print(df)

df = df.iloc[:53].reset_index(drop=True)

df.to_csv("D:\\Visual Studio Codes\\.venv\\Python Scripts\\Data Scraping\\Good Vs. Bad Commit Article.csv", index=False)
print("Successfully Saved into CSV File!")

df = pd.read_csv("D:\\Visual Studio Codes\\.venv\\Python Scripts\\Data Scraping\\Good Vs. Bad Commit Article.csv")


# Funtion to clean content of the text data
def clean_content(text):
    text = re.sub(r'\t+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', ' ', text)
    text = text.strip()

    return text

df['Good Vs. Bad Commit Article'] = df['Good Vs. Bad Commit Article'].apply(clean_content)
print(df)

df.to_csv("D:\\Visual Studio Codes\\.venv\\Python Scripts\\Data Scraping\\Good Vs. Bad Commit Article.csv", index=False)
print("Successfully Saved the Cleaned Data into CSV File!")

csvfile = "D:\\Visual Studio Codes\\.venv\\Python Scripts\\Data Scraping\\Good Vs. Bad Commit Article.csv"

textfile = csvfile.replace('.csv', '.txt')

# Arrays containing element to use for customizing/formatting the text data
subheaders = ['What is a commit?', 'Characteristics of a Good Commit', 'Characteristics of a Bad Commit', 'Best Practices for Good Commits', 'Conclusion']

mainParagraphs = ['Descriptive Commit Message: A descriptive commit message clearly explains what the commit does and why the change was made. It should provide enough context for others (and your future self) to understand the change without reading the code.',
                  'Follow Conventional Commit Guidelines: You can use the standard commit guidelines to keep your git history clean, consistent and easy to read. Usually these guidelines interpret in the form of type (feat, fix, chore, refactor docs), and short summary plus occasionally a long explanation or REF to other relative issues.',
                  'Properly Scoped:Scope your commits appropriately. For instance, if you’re working on a specific feature or fixing a bug, ensure that all changes related to that task are included in a single commit. Avoid partial changes that might leave the codebase in an inconsistent state.',
                  'Vague or Misleading Messages: Commit messages that are vague or misleading do not provide useful information about the changes. This lack of detail can cause confusion and make it hard to track the history of changes.',
                  'Unrelated Changes: Combining unrelated changes into a single commit makes it difficult to isolate specific changes, potentially introducing bugs and complicating the review process.']


with open(textfile, 'w', encoding='utf-8', newline='\n') as text:
    text.write(f"\t\t\t\t\t\t\t'Good Commit ✔ VS. Bad Commit ❌: Best Practices for Git'\n\n")

    for i, row in df.iterrows():
        textRow = row.get('Good Vs. Bad Commit Article', 'No Good Vs. Bad Commit Article')
        
        if textRow in subheaders:
            text.write(f"\n{textRow.upper()}\n")
        
        elif textRow in mainParagraphs:
            text.write(f"\n{textRow}\n")

        else:
            text.write(f"{textRow}\n")

text.close()
os.remove("D:\\Visual Studio Codes\\.venv\\Python Scripts\\Data Scraping\\Good Vs. Bad Commit Article.csv") # Remove CSV File
print("Converted into Text File!")
