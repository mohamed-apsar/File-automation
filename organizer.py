import os
import shutil

class FileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.categories = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
            "Videos": [".mp4", ".mkv", ".avi", ".mov"],
            "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
            "Music": [".mp3", ".wav", ".aac"],
            "Code": [".py", ".js", ".html", ".css", ".java"],
            "Archives": [".zip", ".rar", ".tar", ".gz"],
            "Others": []
        }

    def get_category(self, extension):
        for category, extensions in self.categories.items():
            if extension.lower() in extensions:
                return category
        return "Others"

    def organize(self):
        if not os.path.exists(self.folder_path):
            print(f"Folder not found: {self.folder_path}")
            return
        files_moved = 0
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isdir(file_path):
                continue
            _, extension = os.path.splitext(filename)
            category = self.get_category(extension)
            category_folder = os.path.join(self.folder_path, category)
            os.makedirs(category_folder, exist_ok=True)
            destination = os.path.join(category_folder, filename)
            shutil.move(file_path, destination)
            print(f"Moved: {filename} --> {category}/")
            files_moved += 1
        print(f"Done! {files_moved} files organized.")

    def show_summary(self):
        print("Folder Summary:")
        for folder in os.listdir(self.folder_path):
            folder_path = os.path.join(self.folder_path, folder)
            if os.path.isdir(folder_path):
                count = len(os.listdir(folder_path))
                print(f"  {folder}: {count} file(s)")