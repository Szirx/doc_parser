import streamlit as st
from doc_parser import parse_docx_to_txt


# Streamlit App
st.title('DOCX to TXT Converter')

uploaded_file = st.file_uploader("Upload a DOCX file", type="docx")

if uploaded_file is not None:
    st.write("Processing file...")
    # Parse the DOCX file
    result_txt = parse_docx_to_txt(uploaded_file)
    
    # Offer a download
    st.download_button(
        label="Download TXT file",
        data=result_txt,
        file_name="output.txt",
        mime="text/plain"
    )
    st.write("File processed successfully!")