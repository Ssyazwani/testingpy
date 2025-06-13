import os
import shutil


SOURCE_FOLDER = r"C:\Users\wanio\Downloads"
 


FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'PDFs': ['.pdf'],
    'WordDocs': ['.docx', '.doc'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv'],
    'TextFiles': ['.txt'],
    'Archives': ['.zip', '.rar','.exe'],
    'Scripts': ['.py', '.js', '.java', '.cpp'],
    'Subtitle': ['.ass','.srt'],
    'Others': [] 
}

def get_folder_name(extension):
    for folder, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return folder
    return 'Others'

def organize_files():
    for filename in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, filename)

       
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        folder_name = get_folder_name(ext)

      
        target_folder = os.path.join(SOURCE_FOLDER, folder_name)
        os.makedirs(target_folder, exist_ok=True)

       
        target_path = os.path.join(target_folder, filename)
        shutil.move(file_path, target_path)
        print(f"Moved: {filename} → {folder_name}/")

if __name__ == "__main__":
    print("Organizing files...")
    organize_files()
    print("Done!")
