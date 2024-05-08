# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Files & Exception Handling


def check_blanks(name):
    name = name.replace(" ", "")
    return name


def fix_caps(name):
    name = list(name)
    let = name[0]
    let = let.upper()
    name.remove(name[0])
    name = "".join(name)
    name = (let, name.lower())
    name = "".join(name)
    return name


def check_nums(name):
    name = list(name)
    for char in name:
        try:
            char = float(char)
            print("No numbers, please!")
            carry_on = 0
        except ValueError:
            carry_on = 1
        return carry_on
        

def nameToPig(n1, n2):
    n1 = wordToPig(n1)
    n2 = wordToPig(n2)
    names = n1 + " " + n2
    return names


def wordToPig(n):
    n_list = list(n)
    vowels = list("aeiouAEIOU")
    the_fonz = "ay"

    if n_list[0] in vowels:
        n_list.append(the_fonz)
    else:
        let = n_list[0]
        n_list.remove(n_list[0])
        n_list.append(let + the_fonz)
    n_list = "".join(n_list)
    n_list = fix_caps(n_list)
    return n_list
    

# ============================================ #


while True:
    name_1 = input("Gimme your first name: \n")
    name_2 = input("Gimme your last name: \n")

    name_1 = check_blanks(name_1)
    name_2 = check_blanks(name_2)

    name_1 = fix_caps(name_1)
    name_2 = fix_caps(name_2)

    val_1 = check_nums(name_1)
    val_2 = check_nums(name_2)
    if val_1 != 0 and val_2 != 0:
        break

print(nameToPig(name_1, name_2))
full_name = name_1 + " " + name_2

# add name to text file
file_write = open("names.txt", "a")
print("\n" + full_name, file = file_write, end = "")
file_write.close()

# read names.txt
file_read = open("names.txt", "r")
for line in file_read:
    new_line = list(line)
    index = 0
    for elem in new_line:
        if elem == "\n":
            new_line = new_line[:index]
            
        index +=1
    new_line = "".join(new_line)
    
    # convert to pig latin
    list_line = new_line.split(" ")
    latin_line = nameToPig(list_line[0], list_line[1])

    # write to results_latin.txt
    file_write = open("results_latin.txt", "a")
    print(latin_line, file = file_write)
    file_write.close()
