import whisperx
import gc # garbage collector
import yt_dlp
import os
import subprocess
import re
import spacy
import pandas as pd

# Youtube URL
url = 'https://www.youtube.com/watch?v=3zPCZB5xN8g'

# Directory
output_path = "D:\\Visual Studio Codes"
audio_file = f"{output_path}\\audio_file" # Base name file

start_time = '00:00:00' # start time
end_time = '00:06:34' # end time

# Making sure the directory exists
os.makedirs(output_path, exist_ok=True)

# STEP 1: Convert into a Trimmed MP3 File

try:
    # Webm FIle
    webm_file = os.path.join(output_path, f'{audio_file}.webm')

    ydl_opts = {
        'format' : 'bestaudio[abr>=120]',
        'outtmpl' : webm_file,
        'noplaylist' : True    
    }
    # Download the URL using YoutubeDL with a specific format
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print(f"Successfully Converted into Webm File : {webm_file}")
    
    mp3_file = os.path.join(output_path, f'{audio_file}.mp3')
    
    # Convert into MP3 File
    result = subprocess.run([
        'ffmpeg', '-i', webm_file,
        '-b:a', '128k', mp3_file
    ])

    if result.returncode == 0:
        print(f"Successfully Converted into MP3 File Format : {mp3_file}")
    else:
        print("Unsuccessfully Converted to MP3 File Format")
    
    # Trimmed the MP3 File
    trimmed_mp3_file = os.path.join(output_path, f'{audio_file}_trimmed.mp3')
    
    result = subprocess.run([
        'ffmpeg', '-i', mp3_file,
        '-ss', start_time, '-to', end_time,
        '-c', 'copy', trimmed_mp3_file
    ], capture_output=True, text=True) 

    if result.returncode == 0:
        print(f"Successfully Trimmed the MP3 File : {trimmed_mp3_file}")
    else:
        print("Unsuccessfully Trimmed the MP3 File!")
    
    # Remove the Webm, and MP3 File
    if os.path.exists(webm_file):
        os.remove(webm_file)
    if os.path.exists(mp3_file):
        os.remove(mp3_file)
    

except Exception as e:
    print(f"Error Code : {e}")


# STEP 2 : Load a Model 

audio_file = trimmed_mp3_file

# Specify the parameters of the AI Model
model_name = "base"
device = "cpu"
batch_size = 8
compute_type = "int8"

# Load the model
model = whisperx.load_model(model_name, device, compute_type=compute_type)
audio = whisperx.load_audio(audio_file) # Load the audio file
result = model.transcribe(audio, batch_size=batch_size) # Transcribe the audio 
print(result['segments'])


# Model aligning
model_a, metadata = whisperx.load_align_model(language_code=result['language'], device=device)
result = whisperx.align(result['segments'], 
                        model_a, 
                        metadata,
                        audio,
                        device,
                        return_char_alignments=False)
print(result['segments'])
gc.collect()



# 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

# Use Hugging Face for AI Tokens for the model
diarize_model = whisperx.DiarizationPipeline(use_auth_token='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', device=device)

maxspks = 2
minspks = 1

# Segmentation of the speakers
diarize_segments = diarize_model(audio, min_speakers=minspks, max_speakers=maxspks)

# Assign the speakers
result = whisperx.assign_word_speakers(diarize_segments, result)
print(diarize_segments)
print(result['segments'])


# Get the text of speaker
def get_text_by_speaker(transcription):
    for segment in transcription.get('segments', []):
        speaker = segment.get('speaker')
        text = segment.get('text', '')

        if speaker:
            print(f'{speaker} : {text}')


get_text_by_speaker(result)




# STEP 3 : Clean the Data using SpaCy

nlp = spacy.load('en_core_web_sm')

def clean_transcription(transcription):

    def filter_text(text):
        if len(text.split()) < 1:
            return ''
        return re.sub(r'[.,!?]+$', '', text.strip())
    
    dialogue = []
    for segment in transcription.get('segments', []):
        speaker = segment.get('speaker')
        text = segment.get('text', '').strip()

        sentences = [filter_text(sent.text) for sent in nlp(text).sents]

        for sentence in sentences:
            if sentence:
                dialogue.append(f'{speaker} : {sentence}')
    
    cleaned_transcription = '\n'.join(dialogue)
    return cleaned_transcription

cleaned_transcription = clean_transcription(result)
print(cleaned_transcription)



# STEP 4 : Parse text to df

def parse_text_to_df(text):
    lines = text.strip().split('\n')
    data = {'speaker' : [], 'text' : []}

    for line in lines:
        match = re.match(r'(.+?)\s*:\s*(.*)', line)

        
        if match:
            speaker, text = match.groups()
            data['speaker'].append(speaker)
            data['text'].append(text)
    

    df = pd.DataFrame(data)
    return df

df = parse_text_to_df(cleaned_transcription)
print(df)


# STEP 5 : Drop Column, rename column, and generate keywords

df = df.drop(columns=['speaker'])

df = df.rename(columns={'text' : 'Content'})

df = df[df['Content'].notna() & (df['Content'].str.strip() != '')]

df.to_csv('heyi_youtube_interview.csv', index=False)
print("Successfully Converted into CSV File Format!")

csv_filepath = 'D:\\Visual Studio Codes\\heyi_youtube_interview.csv'

df = pd.read_csv(csv_filepath)

keywords_dict = {
    "Journey": ["officer", "VP", "assistant", "industry"],
    "Growth": ["join", "hired", "create", "leverage"],
    "Education": ["school", "kids", "learning", "culture"],
    "Leadership": ["female", "founder", "team", "strength"],
    "Challenge": ["candidate", "fast", "crypto", "culture"],
    "Innovation": ["disrupt", "tech", "ideas", "change"],
    "Resilience": ["power", "soft", "kindness", "fight"],
    "Passion": ["art", "fashion", "hobby", "interest"],
    "Health": ["fast", "carb", "discipline", "habits"],
    "Community": ["impact", "social", "responsibility", "activism"],
    "Networking": ["connect", "build", "strategic", "support"],
    "Insight": ["wisdom", "knowledge", "experience", "perspective"],
    "Creativity": ["writing", "expression", "dynamic", "ideas"],
    "Awareness": ["education", "mismatch", "training", "fit"],
    "Mindfulness": ["balance", "well-being", "harmony", "focus"],
    "Legacy": ["Satoshi", "influence", "change", "unknown"],
}

def generate_keywords(text):
    keywords = []
    text_lower = text.lower()
    for categories, sub_categories in keywords_dict.items():
        if any(word.lower() in text_lower for word in sub_categories):
            keywords.append(categories)
    
    return ', '.join(keywords)

df['Topic'] = df['Content'].apply(generate_keywords)

df['Topic'] = df['Topic'].replace('', 'He Yi')

df.to_csv('heyi_youtube_interview.txt', index=False, sep='\t')
print("Successfully Scraped!")






































    

       


























    
    

























