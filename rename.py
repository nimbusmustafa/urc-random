import os

def rename_images(input_folder, prefix="imageartag"):
    for count, filename in enumerate(os.listdir(input_folder), 1):
        file_path = os.path.join(input_folder, filename)
        
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            file_ext = os.path.splitext(filename)[1]
            
            new_filename = f"{prefix}_{count}{file_ext}"
            
            # Rename the file
            new_file_path = os.path.join(input_folder, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} to {new_filename}")

if __name__ == "__main__":
    input_folder = "artag_iter2"  # Replace with the path to your folder
    rename_images(input_folder)
