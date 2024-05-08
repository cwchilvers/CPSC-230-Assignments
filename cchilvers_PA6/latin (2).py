# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Pig Latin


def wordToPig(name):
    split_name = name.split(" ")
    first_name = split_name[0]
    last_name = split_name[1]
    pig_name_list = nameToPig(first_name, last_name)
    pig_name = pig_name_list[0] + " " + pig_name_list[1]
    return pig_name


def nameToPig(firstName, lastName):
    check_first = nameCheckCV(firstName)
    check_last = nameCheckCV(lastName)
    canadian = "ay"
    
    # first name
    if check_first == "c":
        pig_first_name = ""
        for char in firstName[1:]:
            pig_first_name += char
        pig_first_name += firstName[0] + canadian
    elif check_first == "v":
        pig_first_name = firstName + canadian
    pig_first_name = fix_caps(pig_first_name)
        
    # last name
    if check_last == "c":
        pig_last_name = ""
        for char in lastName[1:]:
            pig_last_name += char
        pig_last_name += lastName[0] + canadian
    elif check_last == "v":
        pig_last_name = lastName + canadian
    pig_last_name = fix_caps(pig_last_name)
    
    # make list
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
    name = input("Enter a name (First Last): \n")
    blanks = 0
    for char in name:
        if char == " ":
            blanks += 1
    if blanks == 1 and char[0] != " ":
        break


file_write = open("names.txt", "w")
print(name, file = file_write)
file_write.close()


file_read = open("names.txt", "r")
for line in file_read:
    file_write = open("results_latin.txt", "w")
    line = str(line)
    print(wordToPig(line), file = file_write)
    file_write.close()


print(wordToPig(name))
