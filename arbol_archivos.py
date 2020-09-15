#!/usr/bin/env python
import re, sys, os

top_dir = os.path.realpath(sys.argv[0])

print(top_dir)

# Create list of items in directory first
# splitting names at multiple separators
dir_list = [os.path.join(top_dir, re.split("[.-]", f)[0])
            for f in os.listdir(top_dir)
            ]
# Creating set ensures we will have unique
# directory namings
dir_set = set(dir_list)

# Make these directories first
for dir in dir_set:
    if not os.path.exists(dir):
        os.mkdir(dir)

# now get all files only, no directories
files_list = [f for f in os.listdir(top_dir)
              if os.path.isfile(os.path.join(top_dir, f))
              ]

# Traverse lists of directories and files,
# check if a filename starts with directory
# that we're testing now, and if it does - move
# the file to that directory
for dir in dir_set:
    id_string = os.path.basename(dir)
    for f in files_list:
        filename = os.path.basename(f)
        if filename.startswith(id_string):
            new_path = os.path.join(dir, filename)
            print(new_path)
            # os.rename(f,new_path)
