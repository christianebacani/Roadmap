# Libraries
import pandas as pd
import re
import os 
import yt_dlp
import spacy
import subprocess
import whisperx
import gc

# Youtube URL
url = "https://www.youtube.com/watch?v=kYfNvmF0Bqw"

# Directory to store Audio File
directory = "D:\\Visual Studio Codes\\.venv\\Python Scripts"
filepath = f"{directory}\\audio_file"

# Check if the directory exist
os.makedirs(directory, exist_ok=True)

try:
    # Webm File
    webm_file = os.path.join(directory, f"{filepath}.webm")

    # Webm File Format
    ydl_opts = {
        'format' : 'bestaudio[abr>=120]',
        'outtmpl' : webm_file,
        'noplaylist' : True
    }

    # Function to download youtube video with a specific format
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # MP3 File
    mp3_file = os.path.join(directory, f"{filepath}.mp3")

    # Run a subprocess to convert Webm File to MP3 File
    result = subprocess.run([
        'ffmpeg', '-i', webm_file,
        '-b:a', '128k', mp3_file
    ], capture_output=True, text=True)

    # Check if the the subprocess is successful
    if result.returncode != 0 :
        print("Unsuccessfully Converted into MP3 File")
    
    # Remove unncessary files
    os.remove(webm_file)

except Exception as e:
    print(f"Error : {e}")


# WhisperX Model Paramers
model = "base"
device = "cpu"
batch_size = 8
compute_type = "int8"

# Load the WhisperX Model
model = whisperx.load_model(model, device, compute_type=compute_type)
audio = whisperx.load_audio(mp3_file) # Load the audio using the model

# Transcribed the Data
result = model.transcribe(audio, batch_size=batch_size)
print(result['segments']) # Display the transcribe data
gc.collect() # Memory management

# Metadata
model_a, metadata = whisperx.load_align_model(language_code=result['language'], device=device)
# Model Alignments
result = whisperx.align(result['segments'], model_a, metadata, audio, device, return_char_alignments=False)

print(result['segments']) # Display alignments

# Load HF Model
diarize_model = whisperx.DiarizationPipeline(use_auth_token='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', device=device)

# Specify number of speakers
maxspks = 1
minspks = 0

# Segmentation using HF Model
diarize_segments = diarize_model(audio, min_speakers=minspks, max_speakers=maxspks)

# Assign speakers
result = whisperx.assign_word_speakers(diarize_segments, result)
print(result)

# Function to format segmented data
def get_text_by_speaker(transcription):
    # Fetch the segmented data
    for segment in transcription.get('segments', []):
        speaker = segment.get('speaker')
        text = segment.get('text')

        if speaker:
            print(f"{speaker} : {text}")

# Execute the function
get_text_by_speaker(result)

# Load SpaCy Model
nlp = spacy.load('en_core_web_sm')

# Function to clean the formatted data
def clean_content(transcription):
    def filter_text(text):
        if len(text.split()) < 1:
            return ''

        return re.sub(r'[,.!?]*$', '', text)
    
    # Array to store cleaned data
    dialogue = []

    for segment in transcription.get('segments', []):
        speaker = segment.get('speaker')
        text = segment.get('text', '')

        # Clean every rows of text column using Regex and SpaCy Model that is parsed in text format
        sentences = [filter_text(word.text) for word in nlp(text).sents]

        # Loop through the cleaned text column
        for sentence in sentences:
            # Check if there's an instance of cleaned text row in a text column
            if sentence:
                # Add the data from two columns
                dialogue.append(f"{speaker} : {text}")
    
    cleaned_data = '\n'.join(dialogue)
    return cleaned_data # Return the cleaned data when it's executed

# Execute the function
cleaned_transcription = clean_content(result)
print(cleaned_transcription)


# Function to parse cleaned data into Dataframe            
def parse_text_to_df(text):
    # Split every rows into multiple words
    lines = text.strip().split('\n')
    data = {'speaker' : [], 'text' : []}

    for line in lines:
        # Fetch the data if the data is in a specified format (speaker : text)
        match = re.match(r'(\w+)\s*:\s*(.*)', line)

        # Store the data into dictionary if the rows is in a specified format
        if match:
            # Combined the data that is in a specified format
            speaker, text = match.groups()
            
            # Store the combined data into a dictionary
            data['speaker'].append(speaker)
            data['text'].append(text)
    
    # Parse the dict into a dataframe
    df = pd.DataFrame(data)
    return df

# Execute the function
df = parse_text_to_df(cleaned_transcription)
print(df)

# Map the column name
df = df.rename(columns={'speaker' : 'Character', 'text' : 'Content'})

# Map the Character Column value
df['Character'] = df['Character'].replace('SPEAKER_00', 'Steve Jobs')

# Save into CSV File
df.to_csv('steve_jobs_advice.csv', index=False)

# CSV Filepath
csv_filepath = 'D:\\Visual Studio Codes\\steve_jobs_advice.csv'

# Replace the CSV to Text File
textfile = csv_filepath.replace('.csv', '.txt')

# Function to Modify the Text File
with open(textfile, 'w', encoding='utf-8', newline='\n') as text:
    # Iterate through the rows per column
    for i, row in df.iterrows(): 
        character = row.get('Character', 'No Character')
        content = row.get('Content', 'No Content')

        # Write the new content of the new text file based on the text file from a CSV
        text.write(f'{i + 1}. {character} : {content}\n')

print("Successfully Scraped from a Youtube Video!")

# TODO : Execute the script or debug if necessary

            


