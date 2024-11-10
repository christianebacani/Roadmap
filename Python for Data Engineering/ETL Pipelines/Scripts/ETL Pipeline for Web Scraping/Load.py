import pandas as pd
import os

# Load Phase

def load(df):
    # Loading to the target path
    target_filepath = 'D:\\Visual Studio Codes\\Data Engineering Projects in Python\\ETL Pipeline\\Target Data Files\\data_architecture_medium_article.csv'
    df.to_csv(target_filepath, index=False)

    # Prepare the data for conversion    
    df = pd.read_csv(target_filepath)

    textfile = target_filepath.replace('.csv', '.txt')

    # Headers
    headers = ['Key Architectural Principles and Concepts', 'Key Data Architecture Patterns',
               'Additional Resources', 
               'Recap']

    # Sub Headers
    subheaders = ['What is Data Architecture?', 'Evolution of Data Architecture',
                  'Before 2000: The Enterprise Data Warehouse (EDW) Era', 'Characteristics:',
                  'Limitations:', '2000 to 2010: Post-EDW Era',
                  'Characteristics:', '2010 to 2020: The Era of the Logical Data Warehouse (LDW)',
                  'Benefits:', '2020 Onwards: The Era of Augmented Data Analytics and Active Metadata',
                  'Use Cases:', 'Key Architectural Principles and Concepts',
                  'Principles from Leading Enterprises', 'The AWS Well-Architected Framework consists of six pillars:',
                  'Google Cloud’s Five Principles for Cloud-Native Architecture are:', 'Domains and Services', 
                  'Distributed Systems', 'Scalability and Elasticity',
                  'Availability and Reliability', 'Key Metrics:',
                  'Strategies:', 'Event-Driven Architecture',
                  'User Access: Single vs. Multitenant', 'Considerations:',
                  '1. Data Warehouses', '2. Data Lakes', 
                  'Challenges:', '3. Modern Data Stack', 
                  'Components:', '4. Unified Batch and Streaming Architectures', 
                  'Key Architectures:', 'Lambda Architecture:', 
                  'Kappa Architecture:', '5. Data Lakehouse', 
                  '6. Data Mesh', '7. Data Fabric']
    
    # Converting to Text File
    with open(textfile, 'w') as f:
        f.write(f'\t\t\t\t\t\tDATA ARCHITECTURE : A BRIEF OVERVIEW\n\n')
        
        for _, row in df.iterrows():
            content = row.get('Content', 'No Content')

            # Check if the content is headers, subheaders, or paragraph
            if content in headers:
                # Conver the header contents to uppercases
                content = [word.upper() for word in content.split()]
                content = ' '.join(content)

                f.write(f"\n\n\t\t\t\t\t\t{content}\n\n")
            
            elif content in subheaders:
                f.write(f"\n{content}\n\n")
            
            else:
                f.write(f"{content}\n")

    f.close()
    os.remove(target_filepath) # Remove unuse csv file inside the target data files

