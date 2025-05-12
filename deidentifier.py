import os
import shutil 
from pathlib import Path

def create_deidentified_folder (source_folder): 
    if not os.path.isdir(source_folder):
        print(f"The source folder '{source_folder} does not exist")
        return

    parent = "/home/sriram/Documents/Test Folder"
    copy_path = f"{parent}/Test2"

    try:
        shutil.copytree(source_folder, copy_path)
        print(f"Directory copied from '{source_folder}' to '{copy_path}'")
    except FileExistsError:
        print(f"Destination directory '{copy_path}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

orig_dir = input("What is the path of the folder to deidentify?")
create_deidentified_folder(orig_dir)