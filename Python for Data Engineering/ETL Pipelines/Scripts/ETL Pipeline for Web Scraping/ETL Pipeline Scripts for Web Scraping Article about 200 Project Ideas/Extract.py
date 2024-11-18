from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Extract Job

def extract():
    # Web Driver Parameters
    def web_driver():
        options = webdriver.EdgeOptions()
    
        options.add_argument('--verbose')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-settings=1920, 1200')

        driver = webdriver.Edge(options=options)
        return driver

    driver = web_driver()
    driver.get('https://dev.to/kishansheth/200-project-ideas-from-beginner-to-advanced-with-open-source-contributions-3g6a') # URL
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    container = driver.find_elements(By.XPATH, '//div[@class="crayons-article__main "]')

    data = []

    for element in container:
        try:
            data.append(element.text)
        
        except Exception as e:
            print(f"Error Code {e}")

    # Parsed into Dataframe    
    combinedElements = '\n\n'.join(data)
    rows = combinedElements.split('\n')
    df = pd.DataFrame(rows, columns=['Content'])
    
    print("Extracted Data:")
    return df 
