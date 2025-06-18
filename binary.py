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
