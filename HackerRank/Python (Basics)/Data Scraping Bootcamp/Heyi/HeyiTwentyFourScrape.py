import spacy
import pandas as pd
import whisperx
import re
import yt_dlp
import subprocess
import os
import gc

url = 'https://www.youtube.com/watch?v=j8_zU0dNdUw'

directory = 'D:\\Visual Studio Codes'
audio_file = f'{directory}\\audio_file'

start_time = '00:00:39'
end_time = '00:07:19'

os.makedirs(directory, exist_ok=True)

try:
    webm_file = os.path.join(directory, f'{audio_file}.webm')

    ydl_opts = {
        'format' : 'bestaudio[abr>=120]',
        'outtmpl' : webm_file,
        'noplaylist' : True 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    mp3_file = os.path.join(directory, f'{audio_file}.mp3')

    result = subprocess.run([
        'ffmpeg', '-i', webm_file,
        '-b:a', '128k', mp3_file 
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print("Unsuccessfully Converted into MP3 File")
    
    trimmed_mp3_file = os.path.join(directory, f'{audio_file}_trimmed.mp3')

    result = subprocess.run([
        'ffmpeg', '-i', mp3_file,
        '-ss', start_time, '-to', end_time,
        '-c', 'copy', trimmed_mp3_file
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print("Unsuccessfully Trimmed the MP3 File")

    os.remove(webm_file)
    os.remove(mp3_file)

except Exception as e:
    print(f"Error Code : {e}")

model = "medium"
device = "cpu"
batch_size = 12
compute_type = "int8"

model = whisperx.load_model(model, device, compute_type=compute_type)
audio = whisperx.load_audio(trimmed_mp3_file)
result = model.transcribe(audio, batch_size=batch_size)
print(result['segments'])
gc.collect()


model_a, metadata = whisperx.load_align_model(language_code=result['language'], device=device)
result = whisperx.align(result['segments'], model_a, metadata, audio, device, return_char_alignments=False)
print(result['segments'])


diarize_model = whisperx.DiarizationPipeline(use_auth_token='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', device=device)

maxspks = 2
minspks = 1

diarize_segments = diarize_model(audio, min_speakers=minspks, max_speakers=maxspks)

result = whisperx.assign_word_speakers(diarize_segments, result)
print(result['segments'])


def get_text_by_speaker(transcription):
    for segment in transcription.get('segments', []):
        speaker = segment.get('speaker')
        text = segment.get('text', '')

        if speaker:
            print(f"{speaker} : {text}")

get_text_by_speaker(result)

nlp = spacy.load('en_core_web_sm')

def cleaned_transcription(transcription):
    def filter_text(text):
        if len(text.split()) < 1:
            return ''
        return re.sub(r'[.,!?]*$', '', text.strip())
    
    dialogue = []

    for segment in transcription.get('segments', []):
        speaker = segment.get('speaker')
        text = segment.get('text', '').strip()

        sentences = [filter_text(sent.text) for sent in nlp(text).sents]

        for sentence in sentences:
            if sentence:
                dialogue.append(f"{speaker} : {sentence}")
    
    cleaned_transcription = '\n'.join(dialogue)
    return cleaned_transcription

cleaned_transcription = cleaned_transcription(result)
print(cleaned_transcription)

def parse_text_to_df(text):
    lines = text.strip().split('\n')
    data = {'speaker' : [], 'text' : []}

    for line in lines:
        match = re.match(r'(\w+)\s*:\s*(.*)', line)

        if match:
            speaker, text = match.groups()
            data['speaker'].append(speaker)
            data['text'].append(text)
    
    df = pd.DataFrame(data)
    return df

df = parse_text_to_df(cleaned_transcription)
print(df)

df = df.drop(columns=['speaker'])

df = df.rename(columns={'text' : 'Content'})
print(df)


df.to_csv('heyi_interview_blockchain_week.csv', index=False)
print("Successfully Converted into CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_interview_blockchain_week.csv'

df = pd.read_csv(csv_filepath)

keywords_dict = {
    "First Question Spotlight": ["Blockchain", "Dubai", "Binance", "Event", "Week"],
    "Event Vibes": ["Community", "Projects", "Improvement", "Feedback", "Networking"],
    "Startup Mentality": ["Startup", "Growth", "Perfect", "Improve", "Feedback"],
    "Success Story": ["Focus", "Users", "BNB", "Industry", "Build"],
    "BNB Impact": ["BNB", "Life", "Wealth", "Responsibility", "Investment"],
    "Turkish Community": ["Turkish", "Support", "Media", "Presence", "Together"],
    "Crypto Income": ["Blockchain", "Equality", "System", "Undeveloped", "Countries"],
    "Blockchain Impact": ["Blockchain", "Internet", "Transactions", "Assets", "Digital"],
    "DeFi Future": ["Decentralized", "Centralized", "Regulations", "Compliance", "Growth"],
    "Turkey Mention": ["Turkey", "Special", "Future", "Plans", "Visit"],
    "Community Engagement": ["Support", "Feedback", "Interaction", "Events", "Networking"],
    "Innovation Drive": ["Technology", "Change", "Adapt", "Future", "Solutions"],
    "Market Growth": ["Expansion", "Trends", "Investments", "Opportunities", "Success"],
    "User Commitment": ["Trust", "Loyalty", "Satisfaction", "Experience", "Support"],
    "Financial Equity": ["Access", "Opportunity", "Inclusion", "Empower", "Wealth"],
    "Future Vision": ["Goals", "Dreams", "Strategy", "Direction", "Path"],
    "Global Reach": ["International", "Network", "Community", "Impact", "Collaborate"],
    "Regulatory Landscape": ["Compliance", "Policies", "Guidelines", "Stability", "Framework"],
    "Technological Evolution": ["Innovation", "Progress", "Advancement", "Trends", "Revolution"],
    "Cultural Exchange": ["Diversity", "Collaboration", "Influence", "Unity", "Growth"]
}

def generate_keywords(text):
    keywords = []
    text_lower = text.lower()

    for topics, sub_topics in keywords_dict.items():
        if any(word.lower() in text_lower for word in sub_topics):
            keywords.append(topics)
    return ', '.join(keywords)

df['Topic'] = df['Content'].apply(generate_keywords)

df['Topic'] = df['Topic'].replace('', 'He Yi/Yi He')
print(df)

df.to_csv('heyi_interview_blockchain_week.csv', index=False)

filepath = 'D:\\Visual Studio Codes\\heyi_interview_blockchain_week.csv'

text_file  = filepath.replace('.csv', '.txt')

with open(text_file, 'w', encoding='utf-8', newline='\n') as text:
    text.write(f"Content\tTopic\n")

    for i, row in df.iterrows():
        content = row.get('Content', '')
        topic = row.get('Topic', '')
        text.write(f"{i + 1}. {content}:\t{topic}\n")

print("Successfully Scraped a Youtube Video that is converted into Text File!")



