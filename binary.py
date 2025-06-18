import os

root_folder = "your_file.pdf"

for root, dirs, files in os.walk(root_folder):
    for file_name in files:
        if file_name.endswith(".pdf"):
            file_path = os.path.join(root, file_name)
            with open(file_path, "rb") as f:
                binary_data = f.read()
                print(f"Converted: {file_path}")
                print(f"Size: {len(binary_data)} bytes\n")
