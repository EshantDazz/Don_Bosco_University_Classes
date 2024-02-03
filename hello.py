import streamlit as st

# Title for the app
st.title("Text File Viewer")

# Upload a TXT file
txt_file = st.file_uploader("Upload a TXT file", type=["txt"])

if txt_file is not None:
    # Read and display the content of the uploaded TXT file
    content = txt_file.read()
    st.header("File Content:")
    st.text(content)
