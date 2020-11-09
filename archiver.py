from contextlib import suppress
from pathlib import Path
import platform
import os

def move_files(root, dest):
    with suppress(FileExistsError):
        dest.mkdir()

    found_files = list(root.rglob("*.png"))
    for file in found_files:
        print(file)
        os.rename(file, dest / file.name)

def reset_files(root, dest):
    print("Resetting files")
    move_files(dest, root)


if __name__ == "__main__":
    root = Path(r'C:\Users\ashle\Pictures\Saved Pictures')
    dest = root / "dest"

    reset = input("reset? ")

    if reset == "r":
        reset_files(root, dest)
    else:
        move_files(root, dest)