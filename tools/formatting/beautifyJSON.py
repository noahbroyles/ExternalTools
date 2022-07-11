#!/usr/bin/env python3
import sys
import json


file_path = sys.argv[1]

# Read the JSON file
with open(file_path, 'r') as f:
    json_content = json.load(f)

# Write the JSON file with 4 spaces of indentation
with open(file_path, 'w') as f:
    json.dump(json_content, f, indent=4)
