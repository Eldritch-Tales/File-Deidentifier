import os
import shutil 
import re
from pathlib import Path

# Copies input file in order to deidentify it
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

        # Deletes communication log
        delete_files_change_name(deid_path)
    except FileExistsError:
        print(f"Destination directory '{deid_path}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Deletes all files named 'Communication Log' within input directory
def delete_files_change_name(directory):
    # Iterates through all file and directories under the input path
    for file_path in directory.rglob("*"):
        if file_path.is_file() and file_path.stem == "Communication Log":
            try:
                # Deletes the file
                file_path.unlink()
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")
        elif file_path.is_file() and file_path.suffix == ".iom":
            try: 
                trim_name()
            except Exception as e:
                print(f"Failed to rename {file_path}: {e}")

def trim_name(file_path):
    # Extract the part that matches 3 letters + underscore + 6 digits
    match = re.match(r"(\d{6}~[A-Za-z]{3})", file_path.stem)
    if not match:
        print(f"Filename '{file_path.name}' does not match expected pattern.")
        return

    new_stem = match.group(1)
    new_file_path = file_path.with_name(new_stem + file_path.suffix)

    file_path.rename(new_file_path)
    print(f"Renamed to: {new_file_path}")


orig_dir = input("What is the path of the folder to deidentify?")
create_deidentified_folder(orig_dir)