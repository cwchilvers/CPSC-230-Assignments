# Chandler Chilvers
# 2311765
# cchilvers@chapman.edu
# 230-06
# Programming Assignment 7


def encrypt(x):
    global enc_map
    new_string = []
    for char in x:
        if char in enc_map:
            new_string.append(enc_map[char])
        else:
            new_string.append(char)
    new_string = "".join(new_string)
    file_write = open('encrypted.txt', 'a')
    print(new_string, file = file_write, end = "")
    file_write.close()


def decrypt(x):
    global dec_map
    new_string = []
    for char in x:
        if char in dec_map:
            new_string.append(dec_map[char])
        else:
            new_string.append(char)
    new_string = "".join(new_string)
    file_write = open('decrypted.txt', 'a')
    print(new_string, file = file_write, end = "")
    file_write.close()


# open map and create dictionaries
enc_map = {}
dec_map = {}

file_read = open('replace.txt', 'r')
for line in file_read:
    enc_map[line[0]] = line[2]
file_read.close()
file_read = open('replace.txt', 'r')
for line in file_read:
    dec_map[line[2]] = line[0]
file_read.close()


# read unencrypted file and encrypt
file_read = open('lyrics.txt', 'r')
for line in file_read:
    encrypt(line)
file_read.close()


# read encrypted file and decrypt
file_read = open('encrypted.txt', 'r')
for line in file_read:
    decrypt(line)
file_read.close()


