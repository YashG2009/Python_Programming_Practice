# Program que-05.py
# Copy contents of one file to another, replacing all lowercase characters with uppercase

def copy_and_uppercase(src_file, dest_file):
    with open(src_file, 'r') as sf, open(dest_file, 'w') as df:
        for line in sf:
            df.write(line.upper())
    print(f"Copied content from '{src_file}' to '{dest_file}' with lowercase converted to uppercase.")

src_file = "que-05-input/source.txt"
dest_file = "que-05-output.txt"
copy_and_uppercase(src_file, dest_file)
