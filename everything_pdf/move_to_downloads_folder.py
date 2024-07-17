import shutil
import os


# THE BELOW FUNCTION IS THE ONE THAT WILL BE SENT TO THE DOWNLOADS FOLDER

def move_file_to_downloads(source_file):
    try:
        # Ensure the "Downloads" folder exists
        downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
        if not os.path.exists(downloads_folder):
            os.makedirs(downloads_folder)

        # Move the file to the "Downloads" folder
        shutil.move(source_file, downloads_folder)
        print(f"File moved to Downloads folder: {os.path.join(downloads_folder, os.path.basename(source_file))}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example: Replace with the path to the file you want to move
    source_file = "stage.docx"

    move_file_to_downloads(source_file)
