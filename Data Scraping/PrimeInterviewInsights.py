# Import Libraries
import gc
import pandas as pd
import re
import spacy
import whisperx
import yt_dlp
import subprocess
import os

# URL To Scrape
url = 'https://www.youtube.com/watch?v=Q4pglg8b9xY'

# Directory
directory = 'D:\\Visual Studio Codes'
filepath = f'{directory}\\audio_file'

# Timeframe to scrape
start_time = '00:00:00'
end_time = '00:03:22'

# Make sure the directory exists
os.makedirs(directory, exist_ok=True)

try:
    # Webm File
    webm_file = os.path.join(directory, f'{filepath}.webm')

    ydl_opts = {
        'format' : 'bestaudio[abr>=120]',
        'outtmpl' : webm_file,
        'noplaylist' : True
    }
    # Download the Youtube Video using YDL Package and saved into Webm File
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Convert into MP3 File
    mp3_file = os.path.join(directory, f'{filepath}.mp3')

    # Conversion Process
    result = subprocess.run([
        'ffmpeg', '-i', webm_file,
        '-b:a', '128k', mp3_file 
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print("Unsuccessfully Converted into MP3 File Format1")
    
    # Trimmed the MP3 File
    trimmed_mp3_file = os.path.join(directory, f'{filepath}_trimmed.mp3')
    
    # Trimming Process
    result = subprocess.run([
        'ffmpeg', '-i', mp3_file,
        '-ss', start_time, '-to', end_time,
        '-c', 'copy', trimmed_mp3_file 
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print("Unsuccessfully Trimmed!")
    
    # Remove unnecessary files
    os.remove(webm_file)
    os.remove(mp3_file)

except Exception as e:
    print(f"Error Code : {e}")
    

# Customize the Model for Transcribing MP3(Audio)
model = "medium"
device = "cpu"
batch_size = 8
compute_type = "int8"

# Load the model with the paramters using WhisperX
model = whisperx.load_model(model, device, compute_type=compute_type)
audio = whisperx.load_audio(trimmed_mp3_file)
result = model.transcribe(audio, batch_size=batch_size) # Transcribe the audio using model
print(result['segments'])
gc.collect()

# Model Alignments for ASR
model_a, metadata = whisperx.load_align_model(language_code=result['language'], device=device)
result = whisperx.align(result['segments'], model_a, metadata, audio, device)
print(result['segments'])
gc.collect()

# Use Hugging Face Model for Segmentations
diarize_model = whisperx.DiarizationPipeline(use_auth_token='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', device=device)

max_spks = 1
min_spks = 0

# Segmenting Speakers using Hugging Face Model
diarize_segments = diarize_model(audio, min_speakers=min_spks, max_speakers=max_spks)
print(diarize_segments)

# Assign the speaker/s
result = whisperx.assign_word_speakers(diarize_segments, result)
print(result)

# Format the segmented data
def get_text_by_speakers(transcription):
    for segment in transcription.get('segments', []):
        speaker = segment.get('speaker')
        text = segment.get('text', '')

        if speaker:
            print(f"{speaker} : {text}")

get_text_by_speakers(result)

# Load the SpaCy Model for Data Cleaning
nlp = spacy.load('en_core_web_sm')

# Function for Cleaning, Filtering Data
def clean_transcription(transcription):
    def filter_text(text):
        if len(text.split()) < 1:
            return ''
        return re.sub(r'[.,!?]*$', '', text.strip()) # Substitute unneccessary punctuation marks

    dialogue = []

    for segment in transcription.get('segments', []):
        speaker = segment.get('speaker')
        text = segment.get('text', '').strip()

        # Load the data using SpaCy for Cleaning and Filtering
        sentences = [filter_text(sent.text) for sent in nlp(text).sents]

        for sentence in sentences:
            if sentence:
                dialogue.append(f"{speaker} : {sentence}")
    
    cleaned_transcription = '\n'.join(dialogue) # Combined the data for easy parsing
    return cleaned_transcription

cleaned_transcription = clean_transcription(result)
print(cleaned_transcription)

# Function to Parse data into DataFrame
def parse_text_to_df(text):
    lines = text.strip().split('\n')
    data = {'speaker' : [], 'text' : []}

    for line in lines:
        match = re.match(r'(\w+)\s*:\s*(.*)', line) # Parse using Regex Function

        if match:
            speaker, text = match.groups()
            # Load the Parsed Data into a Dictionary
            data['speaker'].append(speaker)
            data['text'].append(text)
    
    # Parse the Dict into DataFrame
    df = pd.DataFrame(data)
    return df

df = parse_text_to_df(cleaned_transcription)
print(df)

# Speaker Mapping
df['speaker'] = df['speaker'].replace('SPEAKER_00', 'Primeagen')

# Drop the Column Name but not the Rows
df = df.rename(columns={'speaker' : 'Speaker',
                        'text' : 'Speech'})

# Save into Text File
df.to_csv('primetime_insights.csv', index=False)

# Access the CSV File
csv_filepath = 'D:\\Visual Studio Codes\\primetime_insights.csv'

text_filepath = csv_filepath.replace('.csv', '.txt')

# Mapped the data from CSV into Text
with open(text_filepath, 'w', encoding='utf-8', newline='\n') as text:
    # Remove the Column Name for Formal Text Data Format
    for i, row in df.iterrows():
        speaker = row.get('Speaker', 'No Speaker')
        speech = row.get('Speech', 'No Speech')
        text.write(f"{speaker}:\t{speech}\n")

# Save the Text File
print("Successfully Scraped!")

