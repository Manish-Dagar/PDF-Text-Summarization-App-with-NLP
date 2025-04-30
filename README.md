# PDF-Text-Summarization-App-with-NLP
PDF Text Summarization App
A Natural Language Processing (NLP) powered application that summarizes PDF documents using Hugging Face's BART model. Built with Python, PyMuPDF for text extraction, and Streamlit for an interactive user interface.
Features

Upload PDF files and generate concise summaries.
Leverages the BART transformer model for high-quality text summarization.
Efficient text extraction with PyMuPDF.
Interactive and user-friendly UI built with Streamlit.
Optimized for handling large PDF documents with minimal latency.

Tech Stack

Python: Core programming language.
Hugging Face Transformers: BART model for summarization.
PyMuPDF: PDF text extraction.
Streamlit: Web app framework for UI.
NumPy/Pandas: Data preprocessing.

Installation

Clone the Repository:
git clone https://github.com/Manish-dagar/PDF-Text-Summarization-App-with-NLP.git
cd pdf-summarization-app


Set Up a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt

Ensure you have requirements.txt with:
streamlit
transformers
torch
PyMuPDF
numpy
pandas


Download the BART Model (if not already cached): The app will automatically download facebook/bart-large-cnn on first run.


Usage

Run the App:
streamlit run app2.py

This will launch the app in your browser (typically at http://localhost:8501).

Upload a PDF:

Use the file uploader to select a PDF document.
The app will extract the text, process it, and display a summary.


View the Summary:

The summarized text will appear below the upload section.



Example

Input PDF: A 10-page research paper.
Output: A 3-4 sentence summary capturing the main ideas.

Project Structure
pdf-summarization-app/
│
├── app.py               # Main Streamlit app script
├── requirements.txt     # Dependencies
├── README.md            # This file
└── utils/               # Helper scripts (e.g., text extraction, preprocessing)

Limitations

Works best with text-based PDFs (scanned PDFs may require OCR).
Summarization quality depends on the PDF's content complexity.
Large PDFs (>50MB) may require additional optimization.

Future Improvements

Add support for multi-document summarization.
Integrate OCR for scanned PDFs.
Deploy the app on a cloud platform like AWS or Heroku.

Contributing
Feel free to fork this repo, submit issues, or create pull requests. Contributions are welcome!
License
This project is licensed under the MIT License - see the LICENSE file for details.

