# Import Libraries
import whisperx
from keybert import KeyBERT
import pandas as pd
import yt_dlp
import subprocess
import spacy
import os
import gc
import re

# URL Youtube Video
url = 'https://www.youtube.com/watch?v=JjHFubUPLV0'

# Directory and Filepath to store File
directory = 'D:\\Visual Studio Codes\\.venv\\Python Scripts'
filepath = f"{directory}\\audio_file"

# Timeframe to scrape
start_time = '00:00:00'
end_time = '10:29'

# Makesure the directory exist
os.makedirs(directory, exist_ok=True)

# Try and catch to handle errors
try:
    # Create a Webm File
    webm_file = os.path.join(directory, f'{filepath}.webm')

    # Format of downloading the Youtube Video
    ydl_opts = {
        'format' : 'bestaudio[abr>=120]',
        'outtmpl' : webm_file,
        'noplaylist' : True
    }

    # Download the Youtube Video then store to the Webm File
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # Specify the Filepath for MP3 File
    mp3_file = os.path.join(directory, f'{filepath}.mp3')

    # Modify as a MP3 File
    result = subprocess.run([
        'ffmpeg', '-i', webm_file,
        '-b:a', '128k', mp3_file 
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print("Unsuccessfully Converted to MP3 File!")

    # Specify the Filepath for Trimmed MP3 File
    trimmed_mp3_file = os.path.join(directory, f'{filepath}_trimmed.mp3')

    # Function to trimmed the mp3 file
    result = subprocess.run([
        'ffmpeg', '-i', mp3_file,
        '-ss', start_time, '-to', end_time,
        '-c', 'copy', trimmed_mp3_file 
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print("Unsuccessfully Trimmed!")
    
    # Remove unncessary files
    os.remove(webm_file)
    os.remove(mp3_file)

# Display a message when error occurs
except Exception as e:
    print(f"Error Code : {e}")

# Model Parameters
model_name = "base"
device = "cpu"
batch_size = 4
compute_type = "int8"

# Load the Model using WhisperX
model = whisperx.load_model(model_name, device, compute_type=compute_type)
audio = whisperx.load_audio(trimmed_mp3_file) # Load the audio

# Transcribe the Audio using the Model
result = model.transcribe(audio, batch_size)
print(result['segments'])

gc.collect()

# Model Alignments
model_a, metadata = whisperx.load_align_model(language_code=result['language'], device=device)

# Aligning Segments
result = whisperx.align(result['segments'], model_a, metadata, audio, device, return_char_alignments=False)
print(result['segments'])

# Using Hugging Face Model for Diariazation
diarize_model = whisperx.DiarizationPipeline(use_auth_token='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', device=device)

# Specify the max and min speakers
maxspks = 1
minspks = 0

# Segmentations of transcribe audio using HF Model
diariaze_segments = diarize_model(audio, min_speakers=minspks, max_speakers=maxspks)
print(diariaze_segments)

# Assigning speakers based on the Diarize Segments and Aligned Model 
result = whisperx.assign_word_speakers(diariaze_segments, result)
print(result['segments'])

gc.collect()

# Functions for structuring Diarized Segments and Aligned Model
def get_text_by_speaker(transcription):
    # Loop through the transcripted audio
    for segment in transcription.get('segments', []):
        speaker = segment.get('speaker')
        text = segment.get('text', '')

        # Format
        if speaker:
            print(f"{speaker} : {text}")

get_text_by_speaker(result)

# SpaCy Model to load the formatted data
nlp = spacy.load('en_core_web_sm')

# Functions to clean the data using SpaCy Model
def clean_transcription(transcription):
    def filter_text(text):
        if len(text.split()) < 1:
            return ''

        # Clean the data using Regex
        return re.sub(r'[,.!?]*$', '', text.strip())

    # Array to store the cleaned data
    dialogue = []

    # Loop to go through each line of formatted data and loaded by SpaCy
    for segment in transcription.get('segments', []):
        speaker = segment.get('speaker')
        text = segment.get('text', '')

        # Clean every lines of data that is loaded by SpaCy
        sentences = [filter_text(word.text) for word in nlp(text).sents]

        # Store in Array for every iteration of data that is clean and loaded using SpaCy and Regex
        for sentence in sentences:
            if sentence:
                dialogue.append(f"{speaker} : {sentence}")

    # Combined the array into single coherent string and return the value
    cleaned_transcription = '\n'.join(dialogue)
    return cleaned_transcription

cleaned_transcription = clean_transcription(result)
print(cleaned_transcription)

# Functions to parse cleaned transcription into Dataframe
def parse_to_df(text):
    # Segment into multiple rows
    lines = text.strip().split('\n')
    data = {'speaker' : [], 'text' : []}

    # Loop through rows and match it with a specified format using Regex
    for line in lines:
        match = re.match(r'(\w+)\s*:\s*(.*)', line)

        # If the rows in loop is matched using regex
        if match:
            # Pass it into two variables
            speaker, text = match.groups()

            # Store the value of the two variables to the dictionary
            data['speaker'].append(speaker)
            data['text'].append(text)
    
    # Parse the dictionary into a df
    df = pd.DataFrame(data)
    return df

df = parse_to_df(cleaned_transcription)
print(df)



# Remove empty rows for two columns
df = df[df['speaker'].str.strip() != ''] 
df = df[df['text'].str.strip() != '']

# Map the speaker column values into a new value
df['speaker'] = df['speaker'].replace('SPEAKER_00', 'Primeagen')

# Map the speaker column name
df = df.rename(columns={'speaker' : 'Character',
                        'text' : 'Speech'})

# Save into CSV File
df.to_csv('primeagen_story.csv', index=False)

# CSV Filepath
csv_filepath = 'D:\\Visual Studio Codes\\primeagen_story.csv'

# Change the file format
txt_filepath = csv_filepath.replace('.csv', '.txt')

# Modify the newly change file format into a specific format text
with open(txt_filepath, 'w', encoding='utf-8', newline='\n') as text:
    for i, row in df.iterrows():
        character = row.get('Character', 'No Character')
        speech = row.get('Speech', 'No Speech')

        text.write(f"{character}:\t{speech}\n")

print("Successfully Scraped!")



