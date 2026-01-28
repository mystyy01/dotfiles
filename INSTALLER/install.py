# make sure you have python>=3.13.7

from __future__ import annotations

from pathlib import Path
import os
import shutil
from datetime import datetime

home = Path.home()
config_folder = Path(os.environ.get("XDG_CONFIG_HOME", home / ".config"))

script_path = Path(__file__).resolve()
repo_root = script_path.parent.parent

backup_root = home / ".dotfiles_backup" / datetime.now().strftime("%Y%m%d-%H%M%S")

config_dirs = {
    "hyprland": config_folder / "hypr",
    "dunst": config_folder / "dunst",
    "rofi": config_folder / "rofi",
    "kitty": config_folder / "kitty",
}

file_targets = {
    repo_root / "git" / "ignore": config_folder / "git" / "ignore",
    repo_root / "home" / ".zshrc": home / ".zshrc",
    repo_root / "home" / ".gitconfig": home / ".gitconfig",
}

print("WARNING: this may overwrite existing configs/files for:\n")
for src, dest in config_dirs.items():
    print(f"- {dest}")
for dest in file_targets.values():
    print(f"- {dest}")

confirmation = input("\nDo you want to continue? (y/N): ")


def backup_existing(path: Path) -> None:
    if not path.exists():
        return
    try:
        rel = path.relative_to(home)
    except ValueError:
        rel = Path("_external") / Path(str(path).lstrip(os.sep))
    backup_path = backup_root / rel
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(path, backup_path)


if confirmation.lower() != "y":
    raise SystemExit(0)

backup_root.mkdir(parents=True, exist_ok=True)
config_folder.mkdir(parents=True, exist_ok=True)

# Install config directories
for src_name, dest in config_dirs.items():
    src = repo_root / src_name
    if not src.exists():
        print(f"Skipping missing: {src}")
        continue
    if dest.exists():
        print(f"Backing up: {dest}")
        backup_existing(dest)
    print(f"Installing: {dest}")
    shutil.copytree(src, dest)

# Install individual files
for src, dest in file_targets.items():
    if not src.exists():
        print(f"Skipping missing: {src}")
        continue
    if dest.exists():
        print(f"Backing up: {dest}")
        backup_existing(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"Installing: {dest}")
    shutil.copy2(src, dest)

print(f"\nDone. Backups stored in: {backup_root}")
