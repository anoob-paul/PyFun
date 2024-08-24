import os
from collections import defaultdict

def find_duplicate_filenames(main_folder):
    # Dictionary to store file information
    files_info = defaultdict(list)
    
    # Walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(main_folder):
        for filename in filenames:
            # Get the full path of the file
            filepath = os.path.join(dirpath, filename)
            # Get the file size
            file_size = os.path.getsize(filepath)
            # Store the file information
            files_info[filename].append({
                'folder_name': os.path.basename(dirpath),
                'folder_path': dirpath,
                'file_size': file_size
            })

    # Print out the duplicate filenames and their details
    for filename, file_details in files_info.items():
        if len(file_details) > 1:
            print(f"\nFile Name: {filename}")
            for detail in file_details:
                print(f"Folder Name: {detail['folder_name']}")
                print(f"Folder Path: {detail['folder_path']}")
                print(f"Size of the File: {detail['file_size']} bytes")
                print("-" * 40)

# Main folder to search in
main_folder = r'C:\Users\Anoob\Pictures'

# Call the function
find_duplicate_filenames(main_folder)
