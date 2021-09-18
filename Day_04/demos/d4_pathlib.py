"""
Demo pathlib module
"""

from pathlib import Path

# Home
print(Path.home())

# Current working directory
print(Path.cwd())

# Data folder (joinpath)
data_folder = Path.home().joinpath("data")
print(data_folder)

# Data folder (nice way)
data_folder_sub = Path.home() / "data" / "subdirectory"
print(data_folder_sub)

# Data file (new way)
file = Path.home() / "data" / "output.csv"
print(file)

# File example
print(file.exists()) # True if the file exist
print(file.name) # The name of the file
print(file.stem) # The name without the extension of the file
print(file.suffix) # The extension of the file
print(file.parent) # The parent directory
print(file.resolve()) # The full path with the name of the file


# Glob
path = Path.cwd() / "Day_04/demos/"
# path = Path("Day_04/demos/")
# print(Path.cwd())
# print(path)
print(list(path.glob("*.py")))
# Recursive glob
path = Path.cwd() / "Day_04/"
print(list(path.rglob("*.py")))

# Reading & writing
text_file = Path("zen.txt")
text_file.write_text("Simple si better tha complex")

print(text_file.read_text())