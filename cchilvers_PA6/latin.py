# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Pig Latin


def wordToPig(name):
    split_name = name.split(" ")
    print(split_name)
    
    # get first name from input
    first_name = split_name[0]

    # get second name from input
    last_name = split_name[1]
    last_name = list(last_name)
            
    # nameToPig
    pig_name_list = nameToPig(first_name, last_name)

    # Get first name from list, add a space, and then add second name from list
    pig_name = pig_name_list[0] + " " + pig_name_list[1]

    # Join list
    pig_name = "".join(pig_name)

    #return the name in pig latin
    return pig_name


def nameToPig(firstName, lastName):
    # check if name starts with con or vowel
    check_first = nameCheckCV(firstName)
    check_last = nameCheckCV(lastName)
    
    the_fonz = "ay"

    
    # FIRST NAME ===========================================================
    # if con
    if check_first == "c":
        pig_first_name = ""
        
        # add all letters after first letter to new name
        for char in firstName[1:]:
            pig_first_name += char
            
        # add first letter to end of new name and then add "ay"
        pig_first_name += firstName[0] + the_fonz

    # if vowel
    elif check_first == "v":
        pig_first_name = firstName + the_fonz

    # send to capitalization function
    pig_first_name = fix_caps(pig_first_name)

        
    # LAST NAME ============================================================
    # (similar to the first name code)
    if check_last == "c":
        pig_last_name = ""
        for char in lastName[1:]:
            pig_last_name += char
        pig_last_name += lastName[0] + the_fonz
    elif check_last == "v":
        pig_last_name = lastName + the_fonz

    # send to capitalization function
    pig_last_name = fix_caps(pig_last_name)

    
    # MAKE LIST =============================================================
    pig_name_list = [pig_first_name, pig_last_name]
    return pig_name_list


def nameCheckCV(name):
    vowels = "aeiouAEIOU"
    status = 0
    if name[0] not in vowels:
        status = "c"
    else:
        status = "v"
    return status


def fix_caps(name):
    first_caps = name[0].upper()
    rest_caps = name[1:].lower()
    name = first_caps + rest_caps
    return(name)


# Prompt user for word:
mode = "enter_name"
while mode == "enter_name":
    name = input("Enter a name (First Last): ")
    blanks = 0
        
    for char in name:
        if char == " ":
            blanks += 1
    if blanks == 1 and char[0] != " ":
        mode = "write"
        break

# ===================== Write ======================= #

# write to file
while mode == "write":
    write_file = open("names.txt", "a")
    file = "names.txt"
    print(name, file = write_file)
    write_file.close()
    break

# ==================== Read ======================== #

read_file = open("names.txt", "r")
write_file2 = open("results_latin.txt", "w")
for line in read_file:
    copy = wordToPig(line)
    print(copy)
    print(copy, file = write_file2)
write_file2.close()
    





