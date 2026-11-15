# File Head Display
# Write a program that asks the user for the name of a file.
# The program should display only the first five (5) lines of the file’s contents. If the file contains fewer than five
# lines, it should display the file’s entire contents.

# Import the files
from pathlib import Path

folder = Path("/Users/kaleiakling/PycharmProjects/COSC-1010-OA-Files")
files = [f.name for f in folder.iterdir() if f.is_file()]

# Display the options
print(f"Available Files: {', '.join(files)}")


while True:
    filename = input("Enter file name including extension or 'quit' to exit: ")
    if filename == "quit":
        break
    try:
        if filename in files:
            with open(folder / filename, "r", encoding="utf-8") as file:
                content = file.readlines()
                cntent = content[:5] if len(content) > 5 else content
                for line in cntent:
                    print(line)
        else:
            print(f"File {filename} not found. Possible file names are: {', '.join(files)}.")

    except FileNotFoundError:
        print("File not found")

