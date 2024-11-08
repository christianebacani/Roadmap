import pandas as pd
from datetime import datetime

# Implementing Simple E.L Data Pipeline

# Extract Data
def extract(data):
    # Initializing the Dataframe to store the read data
    extract_data = pd.DataFrame(columns=['Website Domain', 
                                        'Ticker', 
                                        'Job Opening Title',
                                        'Job Opening URL',
                                        'First Seen At',
                                        'Last Seen At',
                                        'Location',
                                        'Location Data',
                                        'Category',
                                        'Seniority',
                                        'Keywords',
                                        'Description',
                                        'Salary',
                                        'Salary Data',
                                        'Contract Types',
                                        'Job Status',
                                        'Job Language',
                                        'Job Last Processed At',
                                        'O*NET Code',
                                        'O*NET Family',
                                        'O*NET Occupation Name'])

    extracted_data = extract_data._append(pd.read_csv(data, encoding='latin-1')) # Customize the Unicode Representation for capturing larger datasets
    return extracted_data

# Load Data Function
def load(data):
    data.to_csv('D:\\Visual Studio Codes\\Data Engineering Projects in Python\\ETL Pipeline\\Target Data Files\\job_posting.csv')


# Logs Function
def logs(message):
    timestamp_format = '%Y-%m-%d-%H:%M-%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    with open('D:\\Visual Studio Codes\\Data Engineering Projects in Python\\ETL Pipeline\\Log Files\\logfile.txt', 'a', encoding='utf-8') as f:
        f.write(f"{timestamp} : '{message}'\n")


file = 'D:\\Visual Studio Codes\\Data Engineering Projects in Python\\ETL Pipeline\\Source Data Files\\Job Posting.csv'

logs('Extract Data Job Started')
extracted_data = extract(file)
logs('Extract Data Job Ended')

logs('Loading Data Job Started')
load(extracted_data)
logs('Loading Data Job Ended')


