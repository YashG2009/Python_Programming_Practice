# Program que-08.py
# Create another text file deleting the words 'a', 'the', 'an' and replacing them with blank spaces

def remove_words(src_file, dest_file, words_to_remove):
    with open(src_file, 'r') as sf, open(dest_file, 'w') as df:
        for line in sf:
            for word in words_to_remove:
                line = line.replace(f" {word} ", " ")
                line = line.replace(f" {word.capitalize()} ", " ")
            df.write(line)
    print(f"Processed file saved as '{dest_file}'")

src_file = "que-08-input/source.txt"
dest_file = "que-08-output.txt"
words_to_remove = ['a', 'the', 'an']
remove_words(src_file, dest_file, words_to_remove)
