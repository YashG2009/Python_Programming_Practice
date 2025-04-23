# Program que-04.py
# Copy one file from source_subdir to dest_subdir

import os
import shutil

def copy_file(src_path, dest_path):
    if os.path.exists(src_path):
        shutil.copy2(src_path, dest_path)
        print(f"Copied '{src_path}' to '{dest_path}'")
    else:
        print(f"Source file '{src_path}' does not exist.")

src_dir = "que-04-input/source_subdir"
dest_dir = "que-04-output/dest_subdir"
src_file = "sample.txt"
src_path = os.path.join(src_dir, src_file)
dest_path = os.path.join(dest_dir, src_file)
copy_file(src_path, dest_path)
