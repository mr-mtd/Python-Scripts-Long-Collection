import os
import shutil


def organizeFilesInDirs(directory_path):


    # Get a list of all the files in the directory
    file_list = os.listdir(directory_path)

    # Create a list to hold the names of the directories to create
    directory_names = []

    # Loop through each file in the file list
    for filename in file_list:
        # If the file is not a directory itself
        if not os.path.isdir(os.path.join(directory_path, filename)):
            # Append the file name to the list of directory names
            directory_names.append(filename)

    # Loop through each directory name in the list
    for directory_name in directory_names:
        # Create the new directory in the same directory as the file
        directory_path = os.path.join(directory_path, directory_name)
        os.makedirs(directory_path, exist_ok=True)

    # Loop through each file in the file list again
    for filename in file_list:
        # If the file is not a directory itself
        if not os.path.isdir(os.path.join(directory_path, filename)):
            # Get the file path
            file_path = os.path.join(directory_path, filename)
            # Get the directory name for the file
            directory_name = os.path.splitext(filename)[0]
            # Create the new directory path
            new_directory_path = os.path.join(directory_path, directory_name)
            # Create the new directory
            os.makedirs(new_directory_path, exist_ok=True)
            # Move the file to the new directory
            shutil.move(file_path, os.path.join(new_directory_path, filename))


if __name__ == '__main__':
# Set the path to the directory you want to scan
    directory_path = "C:\Users\mason\Documents\CODE_LIBRARY\"
    organizeFilesInDirs(directory_path);