import os
import shutil

archive_folder = 'archive'

# Get all files in the archive folder except the last one
all_files = os.listdir(archive_folder)
if len(all_files) > 1:
    all_files_except_last = all_files[:-1]
else:
    all_files_except_last = []

print("All files except the last one:")
for file_name in all_files_except_last:
    file_path = os.path.join(archive_folder, file_name)
    print(file_path)

# Create '0' and '1' folders in the archive directory
zero_folder = os.path.join(archive_folder, '0')
one_folder = os.path.join(archive_folder, '1')

os.makedirs(zero_folder, exist_ok=True)
os.makedirs(one_folder, exist_ok=True)

# Iterate through the folders inside the archive directory
for folder_name in os.listdir(archive_folder):
    folder_path = os.path.join(archive_folder, folder_name)

    if os.path.isdir(folder_path):
        # Check if the folder name is numeric
        if folder_name.isnumeric():
            zero_path = os.path.join(folder_path, '0')
            one_path = os.path.join(folder_path, '1')

            # Check if '0' and '1' folders exist in the current folder
            if os.path.isdir(zero_path) and os.path.isdir(one_path):
                # Move files from '0' folder to the main '0' folder in the archive
                zero_files = os.listdir(zero_path)
                for file_name in zero_files:
                    file_path = os.path.join(zero_path, file_name)
                    shutil.move(file_path, zero_folder)

                # Move files from '1' folder to the main '1' folder in the archive
                one_files = os.listdir(one_path)
                for file_name in one_files:
                    file_path = os.path.join(one_path, file_name)
                    shutil.move(file_path, one_folder)
