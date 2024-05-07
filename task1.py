import argparse
import os
import shutil
from pathlib import Path

def parse_args():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='Copy files to destination folder, sort into subdirectories based on file extension')

    # Add arguments
    parser.add_argument('source_folder', type=str, help='Source folder path')
    parser.add_argument('--destination_folder', type=str, help='Destination folder path', default="dist")

    # Parse the arguments
    args = parser.parse_args()

    # Access the parsed arguments
    print('source_folder parameter:', args.source_folder)
    print('destination_folder parameter:', args.destination_folder)

    return args

# Function to recursively bypass directories and copy files to destination folder based on extension
def copy_files_by_extension_using_reccursion(src, dest):
    try:
        for entry in os.listdir(src):
                full_path = os.path.join(src, entry)
                if os.path.isdir(full_path):
                    copy_files_by_extension_using_reccursion(full_path, dest)
                else:
                    ext = Path(full_path).suffix[1:] or "no_extension" # Get the file extension
                    target_dir = os.path.join(dest, ext)
                    os.makedirs(target_dir, exist_ok=True) # Create subdirectory if it doesn't exist
                    shutil.copy(full_path, target_dir) # Copy the file to the destination
                    print(f"Copied {full_path} to {target_dir}")
    except FileNotFoundError:
        print(f"{src} directory was not found")
    except PermissionError:
        print("Permission denied")    
    except OSError as ex:
        print(f"OS related error occured. Details -> {ex}")
    except Exception as ex:
        print(f"Unexpected error occured. Details -> {ex}")

# Function to bypass traverse directories and copy files based on extension
def copy_files_by_extension_using_build_in(src, dest):
    for root, dirs, files in os.walk(src):
        for file in files:
            source_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1]  # Get the file extension

            dest_subdir = os.path.join(dest, extension[1:])  # Create subdirectory based on extension
            os.makedirs(dest_subdir, exist_ok=True)  # Create subdirectory if it doesn't exist

            dest_path = os.path.join(dest_subdir, file)
            shutil.copy2(source_path, dest_path)  # Copy the file to the destination

def main():
    args = parse_args()    
    if not os.path.exists(args.source_folder):
        print("Source directory does not exist.")
        return
    if not os.path.exists(args.destination_folder):
        os.makedirs(args.destination_folder)
    copy_files_by_extension_using_reccursion(args.source_folder, args.destination_folder)

if __name__ == "__main__":
    main()
