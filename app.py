import streamlit as st
from pdf_reader import read_pdf
from summarizer import summarize_text

st.title("AI Research Paper Assistant")

uploaded_file = st.file_uploader("Upload a research paper", type="pdf")

if uploaded_file:

    with open("temp.pdf","wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF Uploaded")

    # Read PDF immediately
    text = read_pdf("temp.pdf")

    if st.button("Generate Summary"):

        with st.spinner("Generating summary..."):

            summary = summarize_text(text)

        st.subheader("Summary")

        st.write(summary)