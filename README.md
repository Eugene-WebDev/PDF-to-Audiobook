# PDF-to-Audiobook
PDF to Audiobook Converter
This script converts a PDF file into an audiobook using Google Text-to-Speech (TTS) and combines the audio files into a single MP3 file. It extracts text from the PDF, splits it into chunks, generates audio for each chunk, and then merges them into one final audiobook.

Prerequisites
Python 3.6+

Google Cloud Account with the Text-to-Speech API enabled:

Set up Google Cloud
Enable the Text-to-Speech API
FFmpeg installed:

On Ubuntu/Debian: sudo apt install ffmpeg
On macOS (via Homebrew): brew install ffmpeg
On Windows: Download FFmpeg and add it to your PATH.
Python dependencies:

bash
Copy code
pip install pdfplumber google-cloud-texttospeech
Setup
Google Cloud Authentication:

Set up your Google Cloud project and create a service account key.
Download the JSON credentials file and set the environment variable:
bash
Copy code
export GOOGLE_APPLICATION_CREDENTIALS="path_to_your_service_account_key.json"
Place Your PDF:

Place the PDF file you want to convert in the same directory as this script, or provide its full path.
Usage
1. Run the Script
Execute the Python script with the path to your PDF file:

bash
Copy code
python pdf_to_audiobook.py
2. Input/Output Details
Input: A PDF file (path_to_your_pdf.pdf).
Output:
A folder named after the PDF file will be created (e.g., for your_pdf.pdf, a folder your_pdf/ will be created).
MP3 files will be saved in that folder, with each chunk of the text being converted to an individual MP3 file (chunk_0.mp3, chunk_1.mp3, etc.).
The final audiobook will be combined and saved as <pdf_name>.mp3.
Example
If you have a PDF named sample.pdf, running the script will:

Create a folder named sample/.
Generate MP3 files for each chunk of the PDF.
Combine the MP3 files into a single file: sample/sample.mp3.
Example Command:
bash
Copy code
python pdf_to_audiobook.py
Script Overview
Text Extraction: The script uses the pdfplumber library to extract the text from the provided PDF.
Text-to-Speech: The script utilizes Google Cloud's Text-to-Speech API to convert the extracted text into audio.
Audio Chunking: The text is split into chunks of 5000 bytes (to stay within the API limits), and each chunk is converted to an MP3 file.
FFmpeg: The script then uses FFmpeg to merge the individual MP3 files into one final audiobook.
Troubleshooting
1. Invalid Argument Error (Text Length):
If you encounter an error related to text length exceeding the 5000-byte limit, the script ensures chunks stay within this limit by checking the byte size of each chunk.
2. FFmpeg Not Found:
Ensure FFmpeg is correctly installed and accessible from the command line (ffmpeg -version).
License
This project is licensed under the MIT License - see the LICENSE file for details.
