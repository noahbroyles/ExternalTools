#!/usr/bin/env python3
import sys


file_path = sys.argv[1]

# Open and read the file lines
with open(file_path, 'r') as f:
    file_lines = f.readlines()


import_lines = []
static_import_lines = []
all_import_indexes = []

for lindex in range(0, len(file_lines)):
    line = file_lines[lindex]
    if line.startswith("import") and not line.startswith("import static"):
        import_lines.append(line)
        all_import_indexes.append(lindex)
    elif line.startswith("import static"):
        static_import_lines.append(line)
        all_import_indexes.append(lindex)
        

import_lines = sorted(import_lines, key=lambda x: (len(x), x))
static_import_lines = sorted(static_import_lines, key=lambda x: (len(x), x))

# sort the indexes to get the range
start, stop = all_import_indexes[0], all_import_indexes[-1]

file_lines = file_lines[:start] + import_lines + ['\n' if len(static_import_lines) > 0 else ''] + static_import_lines + file_lines[stop + 1:]


with open(file_path, 'w') as f:
    for line in file_lines:
        f.write(line)
