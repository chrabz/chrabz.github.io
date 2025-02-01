import os

def list_files_in_folder(folder_path, output_file):
    try:
        files = os.listdir(folder_path)
        with open(output_file, "w", encoding="utf-8") as f:
            for file in files:
                file_path = os.path.join(folder_path, file).replace("\\", "/")
                f.write(f'"{file_path}",\n    ')
        print(f"File list saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    folder_path = "C:\Users\elchr\Desktop\WebSite\music"  # Change this to your desired folder
    output_file = "C:\Users\elchr\Desktop\WebSite\music\file_list.txt"
    list_files_in_folder(folder_path, output_file)
