import os

def rename_subfolders(parent_folder):
    for subfolder in os.listdir(parent_folder):
        subfolder_path = os.path.join(parent_folder, subfolder)
        if os.path.isdir(subfolder_path):
            parts = subfolder.split('-')
            if len(parts) >= 3 and parts[0].isdigit():
                # Extract the number and create new name in format CNN-01
                number = parts[0]
                new_name = f"CNN-{number}"
                new_path = os.path.join(parent_folder, new_name)
                os.rename(subfolder_path, new_path)
                print(f"Renamed: {subfolder} -> {new_name}")

rename_subfolders(r'03-CNN')
