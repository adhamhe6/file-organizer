import os
import shutil

def organize_files():
    path = "path/to/your/folder"

    # Change working directory to the specified path
    try:
        os.chdir(path)
    except OSError:
        print(f"Error: Unable to change directory to {path}")
        return

    # Create main folders
    main_folders = {
        'images': ['png', 'jpg', 'jpeg', 'gif'],
        'videos': ['mp4', 'mov', 'avi'],
        'files': ['pdf', 'doc', 'xls', 'txt'],
    }

    # Move files to their respective folders based on extension
    for file in os.listdir('.'):
        if os.path.isfile(file):
            _, file_extension = os.path.splitext(file)
            folder = None
            for main_folder, extensions_list in main_folders.items():
                if file_extension[1:] in extensions_list:
                    folder = main_folder
                    break
            if folder is None:
                folder = 'others'
                if not os.path.exists(folder):
                    os.mkdir(folder)
            if not os.path.exists(os.path.join(folder, file_extension[1:])):
                os.makedirs(os.path.join(folder, file_extension[1:]))
            destination = os.path.join(folder, file_extension[1:], file)
            shutil.move(file, destination)
            print(f"Moving File: {file} to {os.path.join(folder, file_extension[1:])}")

organize_files()