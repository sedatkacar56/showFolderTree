import os
import sys
import io

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

IGNORE_FOLDERS = {"node_modules", "server", ".git", "__pycache__", ".vscode"}
IGNORE_FILES = {"show_folder_tree.bat", "folder_tree.py"}
IGNORE_EXT = {".pyc", ".log"}

def folder_tree(start_path, prefix=""):
    try:
        items = sorted(os.listdir(start_path))
    except PermissionError:
        return
    
    filtered = []
    for item in items:
        path = os.path.join(start_path, item)
        if os.path.isdir(path) and item in IGNORE_FOLDERS:
            continue
        if os.path.isfile(path):
            name, ext = os.path.splitext(item)
            if item in IGNORE_FILES:
                continue
            if ext.lower() in IGNORE_EXT:
                continue
        filtered.append(item)
    
    for i, item in enumerate(filtered):
        path = os.path.join(start_path, item)
        connector = "└── " if i == len(filtered) - 1 else "├── "
        print(prefix + connector + item)
        if os.path.isdir(path):
            new_prefix = prefix + ("    " if i == len(filtered) - 1 else "│   ")
            folder_tree(path, new_prefix)

if __name__ == "__main__":
    folder_path = sys.argv[1].strip().strip('"') if len(sys.argv) > 1 else os.getcwd()
    print("Folder Tree:")
    print()
    folder_tree(folder_path)
