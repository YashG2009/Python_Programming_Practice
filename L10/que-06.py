# Program que-06.py
# Merge lines alternatively from two files and write the results to a new file.
# If one file has fewer lines, remaining lines from the larger file are copied.

def merge_files_alternatively(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        max_len = max(len(lines1), len(lines2))
        for i in range(max_len):
            if i < len(lines1):
                out.write(lines1[i])
            if i < len(lines2):
                out.write(lines2[i])
    print(f"Merged lines alternatively from '{file1}' and '{file2}' into '{output_file}'")

input_dir = "que-06-input"
file1 = f"{input_dir}/file1.txt"
file2 = f"{input_dir}/file2.txt"
output_file = "que-06-output.txt"
merge_files_alternatively(file1, file2, output_file)
