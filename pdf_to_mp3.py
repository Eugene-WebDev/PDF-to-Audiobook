import os
import pdfplumber
from google.cloud import texttospeech
import subprocess

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to split text into byte-safe chunks
def split_text_into_chunks(text, max_bytes=5000, encoding='utf-8'):
    chunks = []
    current_chunk = ""
    for line in text.splitlines():
        line_bytes = line.encode(encoding)
        current_chunk_bytes = current_chunk.encode(encoding)

        if len(current_chunk_bytes) + len(line_bytes) + 1 > max_bytes:
            chunks.append(current_chunk)
            current_chunk = ""
        current_chunk += line + "\n"
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

# Function to convert text to speech and save as MP3
def text_to_speech(text, output_path, chunk_index):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", 
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    file_name = os.path.join(output_path, f"chunk_{chunk_index}.mp3")
    with open(file_name, "wb") as out:
        out.write(response.audio_content)
        print(f"Audio content written to {file_name}")

# Function to merge MP3 files using FFmpeg
def merge_audio_files(output_folder, final_audio_file):
    chunk_files = sorted(
        [f for f in os.listdir(output_folder) if f.startswith("chunk_") and f.endswith(".mp3")]
    )
    list_file = os.path.join(output_folder, "file_list.txt")

    with open(list_file, "w") as f:
        for chunk in chunk_files:
            f.write(f"file '{os.path.join(output_folder, chunk)}'\n")

    command = [
        "ffmpeg", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", final_audio_file
    ]

    print("Merging audio files...")
    subprocess.run(command, check=True)
    print(f"Final audiobook saved to {final_audio_file}")

# Main function to convert PDF to audiobook
def pdf_to_audiobook(pdf_path):
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_folder = os.path.join(os.getcwd(), pdf_name)
    final_audio_file = os.path.join(output_folder, f"{pdf_name}.mp3")

    os.makedirs(output_folder, exist_ok=True)

    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)
    
    print("Splitting text into chunks...")
    chunks = split_text_into_chunks(text)
    
    print("Converting text chunks to audio...")
    for i, chunk in enumerate(chunks):
        text_to_speech(chunk, output_folder, i)
    
    print("Combining audio chunks into a single file...")
    merge_audio_files(output_folder, final_audio_file)
    
    print(f"Audiobook conversion complete! Final file: {final_audio_file}")

# Replace this with the path to your input PDF
pdf_path = "tompkins.pdf"

# Run the conversion
pdf_to_audiobook(pdf_path)

