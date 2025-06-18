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



import os

# Folder where your PDFs are located
folder_path = "your_file.pdf"

# Get list of all PDF files in folder
pdf_files = [file for file in os.listdir(folder_path) if file.endswith(".pdf")]

# Dictionary to store binary content of each PDF
pdf_binaries = {}

for pdf in pdf_files:
    file_path = os.path.join(folder_path, pdf)
    with open(file_path, "rb") as file:
        binary_data = file.read()
        pdf_binaries[pdf] = binary_data

# Now `pdf_binaries` holds each file's binary content
for name, binary in pdf_binaries.items():
    print(f"{name} → {len(binary)} bytes loaded")

