# 📁 Folder Tree Generator

A simple, one-click Windows tool to generate beautiful folder structure visualizations.

## 🌟 Features

- **One-Click Operation** - Just double-click and it works!
- **Clean Output** - Beautiful tree structure with Unicode characters
- **Smart Filtering** - Automatically ignores common clutter (node_modules, .git, etc.)
- **Zero Configuration** - No setup required, works out of the box
- **Lightweight** - Just 2 small files

## 📋 Prerequisites

- Windows OS
- Python 3.x installed ([Download Python](https://www.python.org/downloads/))

## 🚀 Quick Start

### Installation

1. **Download the files:**
   - `folder_tree.py`
   - `show_folder_tree.bat`

2. **Place both files in the folder** you want to analyze

3. **Double-click** `show_folder_tree.bat`

4. **Done!** The output will be saved as `folder_tree_output.txt` and automatically opened in Notepad

## 📖 Example Output

```
Folder Tree:

├── analysis
├── filtered_feature_bc_matrix
├── raw_feature_bc_matrix
├── spatial
├── filtered_feature_bc_matrix.h5
└── raw_feature_bc_matrix.h5
```

## ⚙️ Configuration

You can customize what gets ignored by editing `folder_tree.py`:

```python
IGNORE_FOLDERS = {"node_modules", "server", ".git", "__pycache__", ".vscode"}
IGNORE_FILES = {"show_folder_tree.bat", "folder_tree.py"}
IGNORE_EXT = {".pyc", ".log"}
```

## 💡 Use Cases

- **Documentation** - Document project structures for README files
- **Team Collaboration** - Share folder organization with team members
- **Data Analysis** - Visualize data directory structures
- **Research Projects** - Organize and present research file structures
- **Code Reviews** - Show project organization in code reviews

## 🔧 How It Works

1. The batch file calls the Python script
2. Python recursively scans the directory
3. Generates a tree structure with Unicode box-drawing characters
4. Saves output to a text file
5. Automatically opens the result in Notepad

## 🐛 Troubleshooting

### "Python is not installed or not in PATH"
- Install Python from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation

### "folder_tree.py not found"
- Ensure both files are in the same directory
- Don't rename the files

### Encoding issues
- The tool automatically handles UTF-8 encoding for proper tree character display
- If you see strange characters, make sure you're viewing the output in a UTF-8 compatible editor

## 📝 License

Free to use and modify. No attribution required.

## 🤝 Contributing

Found a bug or have a feature request? Feel free to open an issue!

## 👨‍💻 Author

Created with ❤️ for the community

**Bismillahirrahmanirrahim - Alhamdulillah**

---

⭐ If you find this useful, please star the repository!
