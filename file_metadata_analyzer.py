import os
import time
import csv

def get_file_metadata(file_path):
    try:
        # Get file stats
        stats = os.stat(file_path)

        # Extract file metadata
        file_metadata = {
            'File Path': file_path,  # Use the actual file path passed to the function
            'Size (bytes)': stats.st_size,
            'Creation Time': time.ctime(stats.st_ctime),
            'Last Access Time': time.ctime(stats.st_atime),
            'Last Modification Time': time.ctime(stats.st_mtime),
            'Owner UID': stats.st_uid,
            'Owner GID': stats.st_gid,
            'Permissions': oct(stats.st_mode)[-3:],  # File permissions in octal
            'Inode': stats.st_ino,
            'Device': stats.st_dev
        }

        return file_metadata
    except FileNotFoundError:
        return f"Error: File {file_path} not found."

def print_metadata(file_path):
    metadata = get_file_metadata(file_path)
    if isinstance(metadata, dict):
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print(metadata)

def scan_directory(directory):
    metadata_list = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            metadata = get_file_metadata(file_path)
            if isinstance(metadata, dict):
                metadata_list.append(metadata)
    return metadata_list

if __name__ == "__main__":
    # Specify the file path here
    file_path = '/home/jaanu/file_metadata_analyzer/sampleText.txt'  # Update with your actual file path
    print_metadata(file_path)

    # Optional: Scan a directory for all file metadata
    directory_path = '/home/jaanu/file_metadata_analyzer'  # Correct the indentation here
    files_metadata = scan_directory(directory_path)
    for metadata in files_metadata:
        print(metadata)
