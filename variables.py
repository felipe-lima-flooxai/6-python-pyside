from pathlib import Path

ROOT_DIR = Path(__file__).parent
print("--------")
print(ROOT_DIR)
FILES_DIR = ROOT_DIR / "files"
print(FILES_DIR)
WINDOW_ICON_PATH = FILES_DIR / "icon.ico"