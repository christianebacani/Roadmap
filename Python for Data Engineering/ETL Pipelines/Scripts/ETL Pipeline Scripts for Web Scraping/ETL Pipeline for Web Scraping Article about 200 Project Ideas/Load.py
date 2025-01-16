import pandas as pd
import re
import os 

# Load Job

def load(df):
    target_filepath = 'Target Data Files\\Article about 200 Project Ideas\\200_project_ideas.csv'
    df.to_csv(target_filepath, index=False)

    textfile = target_filepath.replace('.csv', '.txt')

    with open(textfile, 'w', encoding='utf-8', newline='\n') as f:
        f.write(f"\t\t\t\t\t200 Project Ideas from Beginner to Advanced with Open Source Contributions\n")

        df = pd.read_csv(target_filepath)

        subheaders = ['Introduction', '# Project Name Level', 'Conclusion']
    
        for _, rows in df.iterrows():
            content = rows.get('Content', '')
            projectIdea = re.search(r'^(\d)+\.\s(.*):\s(.*)$', content)
            projectIdeaColumn = re.match('^#.', content)

        
            if (content in subheaders) or (projectIdea) or (projectIdeaColumn):
                f.write(f"\n{content}\n")

            else:
                f.write(f"{content}\n")
    

    f.close()
    os.remove(target_filepath) # Remove csv file from the target filepath
    return 'Successfully converted to text file!'

