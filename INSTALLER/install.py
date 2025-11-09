# make sure you have python>=3.13.7

from pathlib import Path
import os
import shutil
home = Path.home()
# change this line if your config directory is not ~/.config/
config_folder = home / ".config"

print("WARNING: this may reset your configs for the following apps: \n")

script_path = Path(__file__).resolve()
parent_dir = script_path.parent.parent

# Get folder names
folders = [f for f in os.listdir(parent_dir) if os.path.isdir(parent_dir / f)]

# Remove folders you don’t want
for skip in [".git", "INSTALLER"]:
    if skip in folders:
        folders.remove(skip)

print(", ".join(folders))

confirmation = input("do you want to continue? (y/N): ")

if confirmation.lower() == "y":
    full_folders = []

    for folder in folders:
        dest = config_folder / folder
        print(dest)
        full_path = parent_dir / folder
        full_folders.append(full_path)
        if dest.exists():
            print(f"⚠️  Removing old config: {dest}")
            shutil.rmtree(dest)
        shutil.copytree(full_path, dest)

else:
    exit()
