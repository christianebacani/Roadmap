from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service  # This imports the Service class
import pandas as pd
import re

def web_driver():
    options = webdriver.EdgeOptions()

    options.add_argument("--verbose")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--blink-settings=imagesEnabled=false")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(executable_path="D:\\Edge WebDriver Folder\\msedgedriver.exe")  # This sets the path to the msedgedriver.exe file
    driver = webdriver.Edge(service=service, options=options)  # This creates a webdriver object with the options and service specified

    return driver

driver = web_driver()
driver.get("https://medium.com/authority-magazine/female-founders-binances-yi-he-on-the-five-things-you-need-to-thrive-and-succeed-as-a-woman-c9786eb33e66")

WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="ab cb"]'))
)

containers = driver.find_elements(By.XPATH, '//div[@class="ab cb"]')

all_data = []

for container in containers:
    paragraphs = container.find_elements(By.XPATH,'.//p')
    for word in paragraphs:
        all_data.append(word.text)

sentences = '\n\n'.join(all_data)

split_sentences = sentences.split('\n')

df = pd.DataFrame(split_sentences, columns=['Content'])

df = df[df['Content'].str.strip() != '']

df.drop_duplicates(inplace=True)

df.to_csv('heyi_medium_article.csv', index=False)

driver.quit()

print("Successfully Saved into CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_medium_article.csv'

df = pd.read_csv(csv_filepath)

df = df.iloc[4:59].reset_index(drop=True)


def clean_content(text):
    text = re.sub(r'\.{2,}', '.', text)             # Replace multiple dots with a single dot
    text = re.sub(r'\s+', ' ', text)                # Replace multiple whitespaces with a single space
    text = re.sub(r'!{2,}', '!', text)              # Replace multiple exclamation marks with one
    text = re.sub(r'\?{2,}', '?', text)             # Replace multiple question marks with one
    text = re.sub(r'-{2,}', '-', text)              # Replace multiple hyphens with a single hyphen
    text = re.sub(r'\n+', ' ', text)                # Replace newlines with space
    text = re.sub(r'\t+', ' ', text)                # Replace tabs with space
    text = re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', text) # Keep only allowed characters
    text = text.strip()                             # Trim leading and trailing spaces
    return text

df['Content'] = df['Content'].apply(clean_content)

keywords_dict = {
    "Introduction": [
        "a part of our series about Women Founders, we had the pleasure of interviewing Yi He.",
        "Yi He is the Co-Founder of Binance, a global blockchain ecosystem behind the world’s largest crypto exchange by trading volume and users."
    ],
    "Background": [
        "I co-founded Binance in 2017 as someone who overcame economic barriers and saw an opportunity to help provide more financial access and freedom for others with crypto and the power of blockchain technology.",
        "Before co-founding Binance, I served as Vice President at Yixia Technology, the leading mobile video tech company behind popular mobile apps like Miaopai, Xiaokaxiu and Yizhibo, where I led branding strategy and marketing operations.",
        "I was also a co-founder of another digital asset exchange between 2014 and 2015. Before joining the blockchain space, I was an anchor for a TV station, and earlier in my career, I was a teacher and assistant psychotherapist.",
        "I come from very humble beginnings and was raised in a small province in China where economic access and opportunities were scarce and higher education was an exception."
    ],
    "Interesting Story": [
        "During my first month at Binance, China went through a policy change and set a ban on crypto exchanges in September 2017.",
        "This led us to exit the market and turn to the global market, requiring me to learn English and adapt to different cultures."
    ],
    "Funny Mistake": [
        "We were one of the first in the industry to help users recover lost or mistakenly sent crypto funds to the wrong address or blockchain network.",
        "Some people in the industry felt that we were being too involved, and while most feedback is positive, some users expect faster resolutions."
    ],
    "Grateful Person": [
        "CZ, the founder and CEO of Binance, has given me direct and constructive feedback, helping me grow and reflect quickly."
    ],
    "Women Founders": [
        "In many industries, the proportion of women in leadership positions is small due to societal expectations and limited encouragement.",
        "I encourage women to seize opportunities, be proactive, and take risks to become successful leaders."
    ],
    "Actions to Overcome Obstacles": [
        "Individuals should cultivate personal abilities, be assertive, and not focus too much on identity.",
        "Society should promote gender diversity in the workplace, provide mentorship, and challenge stereotypes.",
        "At Binance, we support women leadership and provide opportunities for promotion after maternity leave."
    ],
    "Reasons for Women Founders": [
        "True equality will be achieved when there are enough female founders, making the discussion of gender inequality obsolete.",
        "Women should not be constrained by societal norms, and having a diverse team allows for a broader perspective."
    ],
    "Myths About Founders": [
        "Positive myth: Founders' success comes from hard work and endless hours.",
        "Taboo/myth: Successful women use their appearance to gain opportunities, which is a form of discrimination."
    ],
    "Traits for Success": [
        "Successful founders are lifelong learners with ambition, strong execution skills, and the ability to persevere through uncertainty.",
        "Young professionals should start with regular jobs to gain experience and understand themselves and their work better."
    ],
    "Advice for New Founders": [
        "Not dwelling on regrets and accepting all outcomes as part of personal growth.",
        "Failures and difficulties are essential for growth, and experiences should be embraced rather than avoided."
    ],
    "Making the World Better": [
        "Binance helped reshape the crypto industry to be more user-focused and lowered transaction fees.",
        "Created Binance Labs to support and invest in strong projects and startups, managing over $9 billion in assets.",
        "Established Binance Charity to advance transparent philanthropy and contribute to global sustainability efforts."
    ],
    "Inspiring Movement": [
        "Mainstream adoption of crypto will drive financial inclusion and improve lives.",
        "Crypto has the potential to become a standard part of everyday life, similar to mobile phones and electronic payments."
    ],
    "Influential Figures": [
        "Elon Musk for pushing boundaries.",
        "Jeff Bezos for long-term thinking.",
        "Sheryl Sandberg for empowering women.",
        "Lady Gaga and Angelina Jolie for being true to themselves."
    ],
    "Closing Remarks": [
        "Thank you for these fantastic insights. We greatly appreciate the time you spent on this."
    ],
    "Empowerment Trends": [
        "Societal expectations", 
        "Gender diversity", 
        "Leadership barriers", 
        "Proactive approach", 
        "Tech industry opportunities", 
        "Educational advancement", 
        "Career development"
    ],
    "Career Journey": [
        "Co-founder Binance", 
        "Blockchain technology", 
        "Financial access", 
        "Global crypto exchange", 
        "Business strategy", 
        "Incubation and VC arm", 
        "Early-stage challenges", 
        "Economic barriers"
    ],
    "Industry Insights": [
        "Crypto industry evolution", 
        "Decentralized finance (DeFi)", 
        "User-focused approach", 
        "Security and investigations", 
        "Fundraising strategy", 
        "Transparency", 
        "Economic freedom"
    ],
    "Women In Tech": [
        "Female leadership", 
        "Gender equality", 
        "Diversity in tech", 
        "Women founders", 
        "Industry programs", 
        "Mentorship", 
        "Networking opportunities"
    ],
    "Leadership Qualities": [
        "Lifelong learning", 
        "Ambition", 
        "Decision-making", 
        "Execution skills", 
        "Resilience", 
        "Adaptability", 
        "Innovative thinking"
    ],
    "Crypto Vision": [
        "Mainstream adoption", 
        "Financial inclusion", 
        "Global value chain", 
        "Digital transformation", 
        "Philanthropy", 
        "Blockchain impact", 
        "Future of finance"
    ],
    "Inspirational Figures": [
        "Elon Musk", 
        "Jeff Bezos", 
        "Sheryl Sandberg", 
        "Lady Gaga", 
        "Angelina Jolie", 
        "Industry pioneers", 
        "Ambitious leaders"
    ]
}
def generate_keywords(text):
    keywords = []

    for categories, sub_categories in keywords_dict.items():
        if any(sub.lower() in text.lower() for sub in sub_categories):
            keywords.append(categories)

    return ', '.join(keywords)

df['Topic'] = df['Content'].apply(generate_keywords)
df['Topic'] = df['Topic'].replace('', 'He Yi/Yi He')

df.to_csv('heyi_medium_article_keywords.txt', index=False, sep='\t')
print("Successfully Saved into Text File Format!")






