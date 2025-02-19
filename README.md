# PDF to Audiobook Converter

This Python script converts a PDF document into an audiobook (MP3 format). It extracts text from a PDF using [pdfplumber](https://github.com/jsvine/pdfplumber), converts the text into speech with the 
[Google Cloud Text-to-Speech API](https://cloud.google.com/text-to-speech), and finally merges the resulting audio chunks into a single MP3 file using [FFmpeg](https://ffmpeg.org/).

## Features

- **PDF Text Extraction:** Uses pdfplumber to extract text from each page of the PDF.
- **Chunking:** Splits large texts into byte-safe chunks for efficient processing.
- **Text-to-Speech:** Converts each text chunk to speech using Google Cloud’s Text-to-Speech.       
- **Audio Merging:** Combines multiple MP3 audio chunks into one final audiobook file via FFmpeg.   

## Requirements

- **Python 3.x**
- **Python Packages:**
  - [pdfplumber](https://pypi.org/project/pdfplumber/)
  - [google-cloud-texttospeech](https://pypi.org/project/google-cloud-texttospeech/)
- **FFmpeg:** Must be installed and added to your system PATH.
- **Google Cloud Account:** Text-to-Speech API must be enabled.
- **Google Cloud Credentials:** Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to your service account JSON key file.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Install Python Dependencies:**

   You can install the required packages using pip:

   ```bash
   pip install pdfplumber google-cloud-texttospeech
   ```

   Alternatively, if you have a `requirements.txt` file, run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg:**

   - **Windows:** Download FFmpeg from the [official website](https://ffmpeg.org/download.html) and 
add it to your PATH.
   - **macOS:** Install via Homebrew:
     ```bash
     brew install ffmpeg
     ```
   - **Linux:** Install using your package manager, e.g.:
     ```bash
     sudo apt-get install ffmpeg
     ```

4. **Set Up Google Cloud Credentials:**

   Follow the [Google Cloud Text-to-Speech Quickstart](https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries) to download your service account key. Then, set the environment variable:

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
   ```

## Usage

1. **Prepare Your PDF:**
   - Place the PDF you want to convert in the repository directory.
   - Update the `pdf_path` variable in `pdf_to_mp3.py` to point to your PDF file (e.g., replace `"Black Hat Python.pdf"` with your file name).

2. **Run the Script:**

   ```bash
   python pdf_to_mp3.py
   ```

3. **Process Overview:**
   - The script extracts text from the PDF.
   - It splits the text into manageable chunks.
   - Each chunk is converted to an MP3 file.
   - All MP3 chunks are merged into a single audiobook file.
   - The final MP3 is saved in a folder named after the PDF (without its extension).

## Troubleshooting

- **Google Cloud Credentials Error:** Verify that the `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set correctly and points to your JSON key file.
- **FFmpeg Not Found:** Ensure that FFmpeg is installed and its executable is in your system PATH.  
- **PDF Extraction Issues:** Some PDFs may have non-standard formatting that can affect text extraction. Consider preprocessing your PDF if you encounter issues.

## Contributing

Contributions are welcome! If you have suggestions, bug fixes, or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.        

## Acknowledgements

- [pdfplumber](https://github.com/jsvine/pdfplumber) for enabling efficient PDF text extraction.    
- [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech) for the speech synthesis capabilities.
- [FFmpeg](https://ffmpeg.org/) for robust audio processing and merging.
```

This README outlines the purpose, features, setup, and usage instructions of your script. Adjust any sections as needed for your specific project details or personal preferences.


