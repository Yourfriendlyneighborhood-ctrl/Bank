"""
Simple terminal text editor starter for the bankyy workspace.
Run this script to create or edit a file from the terminal.
"""

from pathlib import Path

def main():
    print("Simple Python editor — enter filename to create/edit")
    filename = input("Filename: ").strip()
    if not filename:
        print("No filename provided. Exiting.")
        return

    path = Path(filename)
    if path.exists():
        print(f"\nExisting file contents of {filename}:\n")
        print(path.read_text())
        print("\n--- End of file ---\n")

    print("Enter text to write to the file. Type a single line with .save to save and exit, or .cancel to exit without saving.")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            print("\nEOF received, saving file.")
            break
        if line == ".save":
            break
        if line == ".cancel":
            print("Canceled — not saving.")
            return
        lines.append(line)

    content = "\n".join(lines)
    path.write_text(content)
    print(f"Saved {path.resolve()}")

if __name__ == "__main__":
    main()
