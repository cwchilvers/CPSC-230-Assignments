# Replace lyrics with words input by user

# ask the user for a word to replace & to replace with
to_replace = input("Enter a word to replace within the lyrics: ")
replace_with = input("Enter a word to replace the previous word with: ")

# open the lyrics file to read from
f = open("lyrics.txt", "r")

# open the file to write out the edited lyrics to
g = open("newlyrics.txt", "w")

# read each line of the lyrics file, make changes, write out the results
for line in f:

    # strings are immutable, so have to save the changes to a new variable
    new_line = line.replace(to_replace, replace_with)

    g.write(new_line)

f.close()
g.close()
