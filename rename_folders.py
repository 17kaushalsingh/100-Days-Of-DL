import os

def rename_ann_folders():
    # Get current directory
    current_dir = os.getcwd()
    
    # Find all folders starting with 'ANN-'
    ann_folders = [f for f in os.listdir(current_dir) 
                  if os.path.isdir(f) and f.startswith('CNN-')]
    
    # Print the list of folders
    print("Folders starting with 'CNN-':")
    for folder in ann_folders:
        print(folder)
    
    # Rename the folders by removing 'ANN-' prefix
    for folder in ann_folders:
        new_name = folder[4:]  # Remove 'ANN-' prefix
        old_path = os.path.join(current_dir, folder)
        new_path = os.path.join(current_dir, new_name)
        os.rename(old_path, new_path)
        # print(f"Renamed: {folder} -> {new_name}")

rename_ann_folders() 