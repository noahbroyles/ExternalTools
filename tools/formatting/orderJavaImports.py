#!/usr/bin/env python3
import sys


file_path = sys.argv[1]

# Open and read the file lines
with open(file_path, "r") as f:
    file_lines = f.readlines()


import_lines = []
static_import_lines = []
all_import_indexes = []

# Get which lines are import lines and which are static imports
for lindex in range(0, len(file_lines)):
    line = file_lines[lindex]
    if line.startswith("import") and not line.startswith("import static"):
        import_lines.append(line)
        all_import_indexes.append(lindex)
    elif line.startswith("import static"):
        static_import_lines.append(line)
        all_import_indexes.append(lindex)

# Sort the import lines by length and then alphabetically
import_lines = sorted(import_lines, key=lambda x: (len(x), x))
static_import_lines = sorted(static_import_lines, key=lambda x: (len(x), x))

# Get the range of lines to replace
start, stop = all_import_indexes[0], all_import_indexes[-1]

# Recalculate the file_lines with the ordered import lines
file_lines = (
    file_lines[:start]
    + import_lines
    + ["\n" if len(static_import_lines) > 0 else ""]
    + static_import_lines
    + file_lines[stop + 1 :]
)

# Save the pretty new file
with open(file_path, "w") as f:
    for line in file_lines:
        f.write(line)
