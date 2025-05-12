import os
import shutil 
from pathlib import Path

def create_deidentified_folder (source_folder): 
    source_path = Path(source_folder)

    if not os.path.isdir(source_path):
        print(f"The source folder '{source_path} does not exist")
        return

    parent = source_path.parent
    deid_path = f"{parent}/deid_{source_path.name}"

    try:
        shutil.copytree(source_path, deid_path)
        print(f"Directory copied from '{source_path}' to '{deid_path}'")
    except FileExistsError:
        print(f"Destination directory '{deid_path}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

orig_dir = input("What is the path of the folder to deidentify?")
create_deidentified_folder(orig_dir)