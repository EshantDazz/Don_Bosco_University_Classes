import streamlit as st
import fitz  # PyMuPDF for PDF parsing
import tempfile
from io import BytesIO

# Function to extract text from a PDF file using PyMuPDF
def extract_text_from_pdf(file):
    pdf_text = ""
    if file is not None:
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file_path = f"{temp_dir}/uploaded_file.pdf"

            # Save the uploaded file within the temporary directory
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(file.read())

            # Extract text from the temporary file
            with fitz.open(temp_file_path) as pdf_document:
                for page_number in range(len(pdf_document)):
                    page = pdf_document[page_number]
                    pdf_text += page.get_text()

    return pdf_text

# Create a Streamlit app
st.title("PDF Text Extractor")

# File uploader for PDF files
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Display PDF contents if a file is uploaded
if uploaded_file is not None:
    pdf_contents = extract_text_from_pdf(uploaded_file)
    st.header("PDF Contents:")
    st.text(pdf_contents)
