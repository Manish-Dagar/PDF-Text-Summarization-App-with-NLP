import fitz
import streamlit as st
from io import BytesIO
from transformers import pipeline

# Initialize summarizer globally
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_text_from_pdf(pdf_input):
    try:
        if isinstance(pdf_input, str):
            doc = fitz.open(pdf_input)
        else:  # BytesIO
            doc = fitz.open(stream=pdf_input, filetype="pdf")
        text = ""
        for page in doc:
            page_text = page.get_text()
            if not page_text:  # Fallback for scanned PDFs
                page_text = " ".join([block["text"] for block in page.get_text("dict")["blocks"] if block["type"] == 0])
            text += page_text + "\n"
        return text if text.strip() else "Error: No text extracted from PDF."
    except Exception as e:
        return f"Error extracting text: {str(e)}"
    finally:
        doc.close()

def summarize_text(text, max_length=150, min_length=50, chunk_size=1000):
    try:
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        summaries = []
        for chunk in chunks:
            summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
            summaries.append(summary[0]["summary_text"])
        return " ".join(summaries) if summaries else "Error: Unable to summarize text."
    except Exception as e:
        return f"Error summarizing text: {str(e)}"

st.title("📄 PDF/Notes Summarizer")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
max_length = st.slider("Summary Length (words)", 50, 300, 150)
min_length = st.slider("Minimum Length (words)", 20, 100, 50)

if uploaded_file:
    st.write("📃 Extracting text...")
    pdf_bytes = BytesIO(uploaded_file.read())
    text = extract_text_from_pdf(pdf_bytes)
    if "Error" in text:
        st.error(text)
    else:
        st.write(f"Extracted {len(text.split())} words.")
        st.write("✂️ Summarizing...")
        summary = summarize_text(text, max_length=max_length, min_length=min_length)
        if "Error" in summary:
            st.error(summary)
        else:
            st.subheader("📝 Summary")
            st.write(summary)
            st.write(f"Summary length: {len(summary.split())} words")