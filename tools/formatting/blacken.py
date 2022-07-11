import sys

from black import format_str, FileMode


file_path = sys.argv[1]

# Read the code from the source file
with open(file_path, "r") as f:
    code = f.read()

# Format the code with black
formatted_code = format_str(code, mode=FileMode())

# Write the formatted code back to the source file
with open(file_path, "w") as f:
    f.write(formatted_code)
