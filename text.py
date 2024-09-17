import os
import glob
from os import path


file_names = ["1.txt", "2.txt", "3.txt"]
file_data = {}

for filename in file_names:
    with open(filename, "r") as f:
        lines = f.readlines()
        line_count = len(lines)
        file_content = ' '.join(lines)
        file_data[line_count] = f" {filename} - {line_count} lines\n {file_content}"

sorted_file_data = dict(sorted(file_data.items()))

with open("output.txt", "w") as output_file:
    for _, value in sorted_file_data.items():
        output_file.write(value)