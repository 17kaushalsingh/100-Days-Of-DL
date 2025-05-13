import os

# Directory to scan (current directory)
dir_path = 'data_problem3'

for filename in os.listdir(dir_path):
    if filename.endswith('.jpg.chip.jpg'):
        # Remove the last 9 characters ('.chip.jpg') and add '.jpg'
        new_name = filename[:-9]
        os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_name))
