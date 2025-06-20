import streamlit as st
import os
import base64

# Function to display PDF and show download button
def display_pdf_from_txt(file_path):
    with open(file_path, "r") as f:
        base64_pdf = f.read()

    # Display PDF in iframe
    pdf_viewer = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_viewer, unsafe_allow_html=True)

    # Decode PDF and show download button
    pdf_bytes = base64.b64decode(base64_pdf)
    file_name = os.path.basename(file_path).replace(".txt", ".pdf").replace("_", " ")
    st.download_button(
        label="📥 Download PDF",
        data=pdf_bytes,
        file_name=file_name,
        mime="application/pdf"
    )

# Set page title
st.set_page_config(page_title="Class 10 Notes", layout="centered")
st.title("📚 Class 10 Subject-wise Notes")

# Define the base notes directory
notes_dir = "notes"
notes_structure = {}

# Build dictionary of subjects → chapters → file paths
for subject in os.listdir(notes_dir):
    subject_path = os.path.join(notes_dir, subject)
    if os.path.isdir(subject_path):
        chapters = {}
        for file in os.listdir(subject_path):
            if file.endswith(".txt"):
                chapter_name = file.replace(".txt", "").replace("_", " ").title()
                chapters[chapter_name] = os.path.join(subject_path, file)
        if chapters:
            notes_structure[subject.title()] = chapters

# Step 1: Subject dropdown
subject = st.selectbox("📘 Select Subject", sorted(notes_structure.keys()))

# Step 2: Chapter dropdown
if subject:
    chapters = notes_structure[subject]
    chapter = st.selectbox("📄 Select Chapter", sorted(chapters.keys()))

    # Step 3: Show selected note
    if chapter:
        file_path = chapters[chapter]
        display_pdf_from_txt(file_path)







