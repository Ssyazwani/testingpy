import os
import shutil
import datetime

SOURCE_FOLDER = r"C:\Users\wanio\Downloads"

def organize_by_date():
    for filename in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, filename)

        if os.path.isdir(file_path):
            continue

        timestamp = os.path.getmtime(file_path)
        date = datetime.datetime.fromtimestamp(timestamp)

        folder_name = f"{date.year}-{date.month:02d}"
        target_folder = os.path.join(SOURCE_FOLDER, folder_name)
        os.makedirs(target_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(target_folder, filename))
        print(f"Moved {filename} → {folder_name}/")

if __name__ == "__main__":
    organize_by_date()
