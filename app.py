import streamlit as st
import os
import base64

st.title("Welcome to class 10 PW Hub")
st.title("Here you find All subject All chapter short notes.")

# Set main directory to your notes folder
main_dir = "your_file.pdf"

# List subjects (subdirectories in main directory)
subjects = [d for d in os.listdir(main_dir) if os.path.isdir(os.path.join(main_dir, d))]
selected_subject = st.selectbox("Select a subject", ["biology","physics","chemistry","english","maths","SST"])

# List PDF files for that subject
subject_dir = os.path.join(main_dir, selected_subject)
pdf_files = [f for f in os.listdir(subject_dir) if f.endswith('.pdf')]
selected_file = st.selectbox("Select a PDF", pdf_files)

if selected_file:
    pdf_path = os.path.join(subject_dir, selected_file)

    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')

    # Display PDF in Streamlit
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500px">'
    st.markdown(pdf_display, unsafe_allow_html=True)

    # Provide Download button
    st.download_button(
        label="Download PDF",
        data=pdf_bytes,
        file_name=selected_file,
        mime="application/pdf"
    )


Complaint  = st.text_input("enter your complaint or suggestion :")




