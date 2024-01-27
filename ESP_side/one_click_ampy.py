import subprocess
import os


def upload_files(port, files):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    for file_name in files:
        file_path = os.path.join(current_dir, file_name)

        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue

        print(f"Uploading {file_path} to {port}...")
        try:
            subprocess.run(['ampy', '--port', port, 'put', file_path])
            print("Upload successful!")
        except Exception as e:
            print(f"Error uploading {file_path}: {str(e)}")


if __name__ == "__main__":
    # Specify the serial port of your ESP32 (change it accordingly)
    port = "COM5"  # Update to your actual port

    # Specify the files you want to upload
    files_to_upload = [
        "main.py",
        "program.py",
        "boot.py",
        "program"
        # Add more file names as needed
    ]

    # Upload the files
    upload_files(port, files_to_upload)
