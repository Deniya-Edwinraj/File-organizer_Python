import os
import shutil

def organize_files(source_folder):
    """
    Organize files in the specified folder by file type.
    Creates subfolders for each file type and moves files accordingly.
    """
    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)):
            file_extension = filename.split('.')[-1]
            destination_folder = os.path.join(source_folder, file_extension)

            # Create the folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Move the file to the corresponding folder
            shutil.move(os.path.join(source_folder, filename), os.path.join(destination_folder, filename))
